# -*- coding: utf-8 -*-
# import dbmanager
# https://github.com/Chyroc/WechatSogou
# 复制客户端的历史消息--浏览器--复制浏览器URL
from selenium import webdriver
import selenium
import os
import signal
import urllib2
from collections import deque
import json
from lxml import etree
import httplib
import hashlib
from pybloomfilter import BloomFilter
import thread
import threading
import time
from dbmanager import CrawlDatabaseManager
import re
from mysql.connector import errorcode
import mysql.connector
from lxml.html import clean
from parsedt import parse_datetime
import datetime
from crawl_tools import CrawlTools
from crawl_tools import ScrollStop

# from goose import Goose
# from goose.text import StopWordsChinese
# g = Goose({'stopwords_class': StopWordsChinese})


ctls = CrawlTools()
ctls.chdir_p()

scsp = ScrollStop()

db_manager = CrawlDatabaseManager(10)

pause = 5.5

request_headers = {
    'connection': "keep-alive",
    'cache-control': "no-cache",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'accept-language': "zh-CN,en-US;q=0.8,en;q=0.6"
}

# set custom headers
for key, value in request_headers.iteritems():
    webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = value

cleaner = clean.Cleaner(style=True, scripts=True, comments=True, javascript=True, page_structure=False,
                        safe_attrs_only=False)

# load PhantomJS driver
# driver = webdriver.PhantomJS(executable_path = '/usr/lib/node_modules/phantomjs-prebuilt/lib/phantom/bin/phantomjs',
#                              service_args=['--ignore-ssl-errors=true']) # set window size, better to fit the whole page in order to
driver = webdriver.PhantomJS(
    service_args=['--ignore-ssl-errors=true'])  # set window size, better to fit the whole page in order to
driver.set_window_size(1280, 2400)  # optional

while True:
    db_manager.init_crawl_url()
    c_url = db_manager.dequeue_crawl_url()
    print(c_url)

    if c_url == None:
        break
    else:
        cur_url = c_url['url']
        print(cur_url)

        try:

            driver.get(cur_url)

            scsp.stop_scroll(driver, c_url['catorgy_url'])

            # lastHeight = driver.execute_script("return document.body.scrollHeight")
            # while True:
            #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #     time.sleep(pause)
            #     newHeight = driver.execute_script("return document.body.scrollHeight")
            #     if newHeight == lastHeight:
            #         break
            #     lastHeight = newHeight

            content = driver.page_source

            html_page = driver.page_source
            html_page = html_page.encode('utf-8')

            ## extract content from source
            # print(html_page)
            # print(type(html_page))
            # article = g.extract(raw_html=content)
            # article = g.extract(raw_html=html_page)
            # print(article.cleaned_text.encode('utf-8'))

            # html = etree.HTML(html_page)
            #
            # ctls.getImgList(html_page)

            md5str = c_url['url_md5']

            file_html = md5str + "." + "html"
            file_png = md5str + "." + "png"
            # txtname = md5str + "." + "txt"

            print(os.getcwd())
            ctls.mkdir_p(md5str)

            fo = open("%s/%s" % (md5str, file_html), 'wb+')
            fo.write(html_page)
            fo.close()

            # save png
            driver.save_screenshot("%s/%s" % (md5str, file_png))
            # driver.save_screenshot()
        except:
            next
    db_manager.finish_crawl_url(c_url['id'])


# 1-出队 id + md5 + url
# 2-操作
# 2.1- 存储 html+png+pdf 文件夹名
# 3-done



## python 递归创建文件夹




#
# max_num_thread = 1
#
#
# threads = []
#
#
# cur_url = start_url
#
#
#
# def get_page_content(cur_url, index, depth):
#     try:
#         driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true','--load-images=true']) # or add to your PATH
#         driver.set_page_load_timeout(150)
#         driver.implicitly_wait(60)
#         driver.get(cur_url)
#         time.sleep(10)
#
#         lastHeight = driver.execute_script("return document.body.scrollHeight")
#         while True:
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             time.sleep(pause)
#             newHeight = driver.execute_script("return document.body.scrollHeight")
#             if newHeight == lastHeight:
#                 break
#             lastHeight = newHeight
#
#         print datetime.datetime.now().strftime('%H:%M:%S')
#         fromHeight = 0
#         toHeight = 500
#         step = 500
#         lastHeight = driver.execute_script("return document.body.scrollHeight")
#         while True:
#             jsstr = "window.scrollTo(%d, %d);" % (fromHeight, toHeight)
#             driver.execute_script(jsstr)
#             time.sleep(2)
#             if toHeight + step < lastHeight:
#                 tmp = toHeight
#                 toHeight = step + toHeight
#                 fromHeight = tmp
#             else:
#                 jsstr = "window.scrollTo(%d, %d);" % (toHeight, lastHeight)
#                 driver.execute_script(jsstr)
#                 time.sleep(2)
#                 break
#
#         print datetime.datetime.now().strftime('%H:%M:%S')
#
#         html_page = driver.page_source
#         html_page = html_page.encode('utf-8')
#         html = etree.HTML(html_page)
#         title_new = html.xpath(u'//*[@id="activity-name"]')
#         t_title = title_new[0].text
#         t_title = t_title.replace('\n', '')
#         t_title = t_title.replace('\t', '')
#         t_title = t_title.replace(' ', '')
#         date_new = html.xpath(u'//*[@id="post-date"]')
#         t_date = date_new[0].text
#         dbmanager.updateTitle(index, t_title)
#
#         md5str = t_title+t_date
#         md5str = md5str.encode('utf-8')
#         md5str = hashlib.md5(md5str).hexdigest()
#
#         filename = md5str + "." + "html"
#         pngname = md5str + "." + "png"
#         txtname = md5str + "." + "txt"
#
#         fo = open("%s%s" % (dir_name, filename), 'wb+')
#         fo.write(html_page)
#         fo.close()
#
#         # save png
#         driver.save_screenshot("%s%s" % (pic_name, pngname))
#         dbmanager.finishUrl(index)
#
#     except urllib2.HTTPError, Arguments:
#         print Arguments
#         return
#     except httplib.BadStatusLine, Arguments:
#         print Arguments
#         return
#     except IOError, Arguments:
#         print Arguments
#         return
#     except Exception, Arguments:
#         print Arguments
#         return
#
#     os.system('pgrep phantomjs | xargs kill')
#
#
#
# while True:
#     curtask = dbmanager.dequeueUrl()
#     # Go on next level, before that, needs to wait all current level crawling done
#     if curtask is not None:
#         print(curtask)
#         get_page_content(curtask['url'], curtask['index'], curtask['depth'])
#     else:
#         break
