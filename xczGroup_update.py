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

request_headers = {
    # 'host': "tzs.ndrc.gov.cn",
    'connection': "keep-alive",
    'cache-control': "no-cache",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'accept-language': "zh-CN,en-US;q=0.8,en;q=0.6"
}

start_url = "https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzI0MDM1ODE4Mg==&scene=124&uin=MjQwMTUyNzQ2Mw%3D%3D&key=f9e33d239d58dedcb36703a535a78db6ed9457f9f52b74920061fa0d3d3c65daf836a71974169bdc89ab9a2f3265b98b3facbfba664bd958d1102e28ca5bb433cbd57a0e514fe02cd41d109c28bf6c21&devicetype=iMac+MacBookPro11%2C4+OSX+OSX+10.12.4+build(16E195)&version=12020510&lang=zh_CN&nettype=WIFI&a8scene=0&fontScale=100&pass_ticket=wK86ckUWxdWD6MFiafGwoTB22ob1xyAhuw7kG%2BQ7bt8auK9IbladuHs7IAUFCuot"
url_domain = "xczgroup"


# set custom headers
for key, value in request_headers.iteritems():
    webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = value

cleaner = clean.Cleaner(style=True, scripts=True, comments=True, javascript=True, page_structure=False,
                        safe_attrs_only=False)

# # ignore ssl error, optionally can set phantomjs path
# driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true']) # or add to your PATH
#
# # set bigger windows height to dynamically load more data
# driver.set_window_size(1280, 2400) # optional

# dir for saving HTML files
dir_name = 'src_html/'
# dir for saving doc files
doc_name = 'src_content/'
# dir for saving doc files
pic_name = 'src_img/'



# time delay before a new crawling thread is created
# use a delay to control the crawling rate, avoiding visiting target website too frequently
# 设置超时，控制下载的速率，避免太过频繁访问目标网站
CRAWL_DELAY = 0.1
pause = 5.5

max_num_thread = 1

# create instance of Mysql database manager, which is used as a queue for crawling
dbmanager = CrawlDatabaseManager(max_num_thread)

# update
dbmanager.updateCrawl(url_domain)

# put first page into queue
dbmanager.enqueueUrl(start_url, 0, url_domain, None, None, None)
start_time = time.time()
is_root_page = True
threads = []

cur_url = start_url

# ignore ssl error, optionally can set phantomjs path
driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'])  # or add to your PATH
# set bigger windows height to dynamically load more data
# driver.set_window_size(1280, 2400) # optional
# driver.set_page_load_timeout(50)
# driver.implicitly_wait(20)
driver.get(cur_url)

lastHeight = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(pause)
    newHeight = driver.execute_script("return document.body.scrollHeight")
    if newHeight == lastHeight:
        break
    lastHeight = newHeight

# req = urllib2.Request(cur_url, headers=request_headers)
# response = urllib2.urlopen(req)

html_page = driver.page_source
html_page = html_page.encode('utf-8')
html = etree.HTML(html_page)

hrefs = html.xpath(u'//*[@class="weui_media_bd"]/h4')
# hrefs = html.xpath(u'//*[@class="weui_media_bd"]/h4/@hrefs')
len(hrefs)

desc = html.xpath(u'//*[@class="weui_media_bd"]/p[@class="weui_media_desc"]')
len(desc)

url_date = html.xpath(u'//*[@class="weui_media_bd"]/p[@class="weui_media_extra_info"]')
len(url_date)

for i in range(len(url_date)):
    t_url = hrefs[i].attrib['hrefs']
    t_title = hrefs[i].text
    t_title = t_title.replace('\n', '')
    t_title = t_title.replace('\t', '')
    t_title = t_title.replace(' ', '')
    t_date = parse_datetime(url_date[i].text).strftime('%Y-%m-%d')
    t_desc = desc[i].text
    t_desc = t_desc.replace('\n', '')
    t_desc = t_desc.replace('\t', '')
    dbmanager.enqueueUrl(t_url, 1, url_domain, t_desc, t_title, t_date)


def get_page_content(cur_url, index, depth):
    try:
        driver = webdriver.PhantomJS(
            service_args=['--ignore-ssl-errors=true', '--load-images=true'])  # or add to your PATH
        driver.set_page_load_timeout(150)
        driver.implicitly_wait(60)
        driver.get(cur_url)
        time.sleep(10)

        lastHeight = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(pause)
            newHeight = driver.execute_script("return document.body.scrollHeight")
            if newHeight == lastHeight:
                break
            lastHeight = newHeight

        print datetime.datetime.now().strftime('%H:%M:%S')
        fromHeight = 0
        toHeight = 500
        step = 500
        lastHeight = driver.execute_script("return document.body.scrollHeight")
        while True:
            jsstr = "window.scrollTo(%d, %d);" % (fromHeight, toHeight)
            driver.execute_script(jsstr)
            time.sleep(2)
            if toHeight + step < lastHeight:
                tmp = toHeight
                toHeight = step + toHeight
                fromHeight = tmp
            else:
                jsstr = "window.scrollTo(%d, %d);" % (toHeight, lastHeight)
                driver.execute_script(jsstr)
                time.sleep(2)
                break

        print datetime.datetime.now().strftime('%H:%M:%S')

        html_page = driver.page_source
        html_page = html_page.encode('utf-8')
        html = etree.HTML(html_page)
        title_new = html.xpath(u'//*[@id="activity-name"]')
        t_title = title_new[0].text
        t_title = t_title.replace('\n', '')
        t_title = t_title.replace('\t', '')
        t_title = t_title.replace(' ', '')
        date_new = html.xpath(u'//*[@id="post-date"]')
        t_date = date_new[0].text
        dbmanager.updateTitle(index, t_title)

        md5str = t_title + t_date
        md5str = md5str.encode('utf-8')
        md5str = hashlib.md5(md5str).hexdigest()

        filename = md5str + "." + "html"
        pngname = md5str + "." + "png"
        txtname = md5str + "." + "txt"

        fo = open("%s%s" % (dir_name, filename), 'wb+')
        fo.write(html_page)
        fo.close()

        # save png
        driver.save_screenshot("%s%s" % (pic_name, pngname))
        dbmanager.finishUrl(index)

    except urllib2.HTTPError, Arguments:
        print Arguments
        return
    except httplib.BadStatusLine, Arguments:
        print Arguments
        return
    except IOError, Arguments:
        print Arguments
        return
    except Exception, Arguments:
        print Arguments
        return

    os.system('pgrep phantomjs | xargs kill')


while True:
    curtask = dbmanager.dequeueUrl()
    # Go on next level, before that, needs to wait all current level crawling done
    if curtask is not None:
        print(curtask)
        get_page_content(curtask['url'], curtask['index'], curtask['depth'])
    else:
        break


# driver.close()
#
# driver.quit()
