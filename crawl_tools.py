# -*- coding: utf-8 -*-

import time
import os, errno
import urllib
import urllib2
import re
from lxml import etree
from goose import Goose
from goose.text import StopWordsChinese
from parseDate import DateExtract
from textrank4zh import TextRank4Keyword, TextRank4Sentence
import codecs
import pandas as pd
import mysql.connector as sql

d_ext = DateExtract()

g = Goose({'stopwords_class': StopWordsChinese})


class CrawlTools:
    # DIR_CRAWL = 'jc_crawl'
    # SERVER_IP = '172.16.0.116'
    # TABLES = {}
    # /Users/xuweiyun/Desktop/jc/project/jcCrawler/crawl_dequeue.py
    # DIR_CRAWL = '/Users/xuweiyun/Desktop/jc/project/jcCrawler/testdir'
    # REG_IMG = r'src="(.+?\.jpg|JPG|PNG|png)"'
    # REG_IMG = re.compile(REG_IMG)

    def __init__(self):
        self.DIR_CRAWL = '/Users/xuweiyun/Desktop/jc/project/jcCrawler/testdir'
        REG_IMG = r'src="(.+?\.jpg|JPG|PNG|png)"'
        self.REG_IMG = re.compile(REG_IMG)
        self.headers = {
            'connection': "keep-alive",
            'cache-control': "no-cache",
            'upgrade-insecure-requests': "1",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            'accept-language': "zh-CN,en-US;q=0.8,en;q=0.6"
        }

    # parse baidu url to actual url
    def real_url(self, url):
        try:
            req = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(req)
            realurl = response.geturl()
        except:
            realurl = ''
        return realurl

    def find_url(self, e):
        ea = e.xpath('h3/a')
        if (len(ea) > 0):
            ea = ea[0]
            if 'href' in ea.attrib:
                return ea.attrib['href']
            else:
                return
        else:
            return

    def noneurl(self, e):
        if e is None:
            return False
        else:
            return True

    # mkdir -p
    def mkdir_p(self, path):
        try:
            os.makedirs(path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise

    # chdir to crawl dir
    def chdir_p(self):
        if os.path.exists(self.DIR_CRAWL):
            os.chdir(self.DIR_CRAWL)
        else:
            self.mkdir_p(self.DIR_CRAWL)
            os.chdir(self.DIR_CRAWL)

    def getImgList(self, html):
        imglist = re.findall(self.REG_IMG, html)
        print(imglist)


# import urllib
# import re
#
# def getHtml(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     return html
#
# def getImgList(html):
#     reg = r'src="(.+?\.jpg|JPG|PNG|png)"'
#     imgre = re.compile(reg)
#     imglist = re.findall(imgre,html)
#     print(imglist)
#     x = 0
#     for imgurl in imglist:
#         urllib.urlretrieve(imgurl,'%s.jpg' % x)
#         x+=1
#
#
# html = getHtml("http://tieba.baidu.com/p/2460150866")
#
# print getImg(html)


#############
## render pdf
# from selenium import webdriver
# def execute(script, args):
#     driver.execute('executePhantomScript', {'script': script, 'args' : args })
#
# driver = webdriver.PhantomJS('phantomjs')
#
# # hack while the python interface lags
# driver.command_executor._commands['executePhantomScript'] = ('POST', '/session/$sessionId/phantom/execute')
#
# driver.get('http://finance.qq.com/original/caijingguancha/f1484.html')
#
# # set page format
# # inside the execution script, webpage is "this"
# pageFormat = '''this.paperSize = {format: "A4", orientation: "portrait" };'''
# execute(pageFormat, [])
#
# # render current page
# render = '''this.render("test.pdf")'''
# execute(render, [])


# 将向下滚动包装为一个具体的类，避免 类似 www.sohu.com 滚动太长或出现跳转的情况
class ScrollStop:
    def __init__(self):
        self.PAUSE = 5.5
        self.TESTTAGS = {'www.sohu.com': u'//*[@class="article-oper"]//text()'}

    # parse baidu url to actual url
    def stop_scroll(self, driver, catgory_url):
        try:
            lastHeight = driver.execute_script("return document.body.scrollHeight")
            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(self.PAUSE)
                newHeight = driver.execute_script("return document.body.scrollHeight")
                print(newHeight)

                if (catgory_url in self.TESTTAGS):
                    html_page = driver.page_source
                    html_page = html_page.encode('utf-8')
                    html = etree.HTML(html_page)

                    testTag = html.xpath(self.TESTTAGS[catgory_url])
                    testTag = ''.join(testTag)

                    if newHeight == lastHeight or lastHeight > 20000 or testTag <> '':
                        break
                    lastHeight = newHeight
                else:
                    if newHeight == lastHeight:
                        break
                    lastHeight = newHeight
            return True
        except:
            return False



# 文本解析（日期、标题、正文）
class HtmlExtract:
    def __init__(self):
        self.PAUSE = 5.5
        self.FPATH = '/home/jc/crawlDir/'
        # self.FPATH = '/home/jc/projectJC/crawler/back_conf/exam'

    # get tags xpath info
    # def get_xpath(self, catgory_url):

    # parse baidu url to actual url
    def url_extract(self, url_md5, catgory_url, url):
        rest_dict = {
            'url_releasetime': None,
            'url_title': None,
            'url_content': None,
            'ext_phrase': None,
            'ext_sentence': None,
            'pth_html': None
        }

        filepath = self.FPATH + url_md5 + '/' + url_md5 + '.html'

        db_connection = sql.connect(host='172.16.0.116', database='jc_crawl', user='root', password='jcplanb.com')
        df = pd.read_sql(
            'SELECT xpath_name, xpath_p FROM tags_xpath where status = 1 and catorgy_url = "%s"' % catgory_url,
            con=db_connection)
        db_connection.close()

        tags = df.groupby('xpath_name')['xpath_p'].apply(lambda x: ' | '.join(x))
        # print(tags)

        if tags.shape[0] == 0:
            tags = None
        else:
            tags = tags.to_dict()
        # print(tags)

        # filepath exist or not
        if os.path.exists(filepath):
            raw_html = codecs.open(filepath, 'r', 'utf-8').read()
            g_content = g.extract(raw_html=raw_html)
            # print(type(g_content))
            tr = etree.HTML(raw_html)
            # print(type(tr))
            if tags:
                release_time = tr.xpath(tags['release_time'])
                url_title = tr.xpath(tags['url_title'])
                url_content = tr.xpath(tags['url_content'])
                if len(release_time) > 0:
                    release_time = ''.join(release_time)
                    release_time = d_ext.extractUrlDate(release_time)
                else:
                    release_time = None

                if len(url_title) > 0:
                    url_title = url_title[0]
                    url_title = url_title.strip()
                    url_title = re.sub('\s+', '', url_title)
                else:
                    url_title = None

                if len(url_content) > 0:
                    url_content = map(lambda x: x.strip(), url_content)
                    url_content = map(lambda x: re.sub('\s{3,}', '\n', x), url_content)
                    url_content = map(lambda x: re.sub('\s{2}', '', x), url_content)
                    url_content = '\n'.join(url_content)
                else:
                    url_content = None
            else:
                release_time = None
                url_title = None
                url_content = None

            if release_time is None:
                release_time = d_ext.extractUrlDate(url)

            if url_title is None:
                url_title = g_content.title

            if url_content is None:
                url_content = g_content.cleaned_text

            if url_content is not None:
                # ext_phrase
                tr4w = TextRank4Keyword()
                tr4w.analyze(text=url_content, lower=True, window=2)

                phrase = tr4w.get_keyphrases(keywords_num=10, min_occur_num=2)
                if len(phrase) > 0:
                    ext_phrase = ','.join(phrase)
                else:
                    ext_phrase = None


                # ext_sentence
                tr4s = TextRank4Sentence()
                tr4s.analyze(text=url_content, lower=True, source='all_filters')
                sentences = tr4s.get_key_sentences(num=3)
                if len(sentences) > 0:
                    sentences = map(lambda x: x.sentence, sentences)
                    ext_sentence = '。'.join(sentences)
                else:
                    ext_sentence = None

            rest_dict['url_releasetime'] = release_time
            rest_dict['url_title'] = url_title
            rest_dict['url_content'] = url_content
            rest_dict['ext_phrase'] = ext_phrase
            rest_dict['ext_sentence'] = ext_sentence
            rest_dict['pth_html'] = url_md5 + '/' + url_md5 + '.html'


            # print("release_time")
            # print(release_time)
            # print("url_title")
            # print(url_title)
            # print("url_content")
            # print(url_content[1:300])
            # print("ext_phrase")
            # print(ext_phrase)
            # print("ext_sentence[1:300]")
            # print(ext_sentence[1:300])
        return rest_dict
