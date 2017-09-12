# -*- coding: utf-8 -*-

import time
import os, errno
import urllib
import urllib2
import re
from lxml import etree


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

    # parse baidu url to actual url
    def real_url(self, url):
        try:
            response = urllib2.urlopen(url)
            realurl = response.geturl()
        except:
            realurl = ''
        return realurl

    def find_url(self, e):
        ea = e.xpath('h3/a')
        if(len(ea) > 0):
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
            else: raise

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

                if(catgory_url in self.TESTTAGS):
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


