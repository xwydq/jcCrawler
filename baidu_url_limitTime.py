# -*- coding: utf-8 -*-

from selenium import webdriver
from urllib import quote
from urllib import unquote
from lxml import etree
from lxml.html import clean
import time
import pandas as pd
import numpy as np
from dbmanager import CrawlDatabaseManager
import hashlib
import sys
import urllib2
from crawl_tools import CrawlTools

reload(sys)
sys.setdefaultencoding('utf8')

ctls = CrawlTools()

db_manager = CrawlDatabaseManager(10)
pause = 5.5
# keywords = [u"金诚集团", u"PPP", u"特色小镇", u"金诚新城镇", u"金诚财富"]
keywords = ["金诚集团", "PPP", "特色小镇", "金诚新城镇", "金诚财富"]
keywords = map(lambda x: quote(x), keywords)
# print(keywords)


# 时间戳
# 搜索近几天的数据
sday = 7
cur_time = int(time.time())
stime_from = cur_time - sday * 24 * 60 * 60
stime_to = cur_time
stime_range = 'gpc=stf%%3D%s%%2C%s%%7Cstftype%%3D1' % (stime_from, stime_to)
# print(stime_from)
# print(stime_to)

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
    db_manager.init_catorgy_url()
    c_url = db_manager.dequeue_catorgy_url()

    if c_url == None:
        break
    else:
        catorgy_url = c_url['catorgy_url']
        print(catorgy_url)

        for kwords_i in keywords:
            print(unquote(kwords_i))
            search_url = '&wd="%s" site:%s' % (kwords_i, catorgy_url)
            # print(search_url)
            cur_url = "https://www.baidu.com/s?" + stime_range + search_url
            print(cur_url)

            while True:
                driver.get(cur_url)

                lastHeight = driver.execute_script("return document.body.scrollHeight")
                while True:
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(pause)
                    newHeight = driver.execute_script("return document.body.scrollHeight")
                    if newHeight == lastHeight:
                        break
                    lastHeight = newHeight

                content = driver.page_source

                html_page = driver.page_source
                html_page = html_page.encode('utf-8')
                html = etree.HTML(html_page)

                no_result = html.xpath(u'//*[@id="container"]/div[2]/div/p/text()')
                more_page = html.xpath(u'//*[@id="page"]/a')

                # print(len(more_page))

                if (len(more_page) > 0):
                    more_page_content = map(lambda x: ''.join(x.itertext()).strip(), more_page)
                    next_page = filter(lambda x: x == u'下一页>', more_page_content)
                    if len(next_page) > 0:
                        next_page = more_page[-1]
                        next_page = "https://www.baidu.com" + next_page.attrib['href']
                    else:
                        next_page = None
                    cur_url = next_page
                else:
                    next_page = None

                if (len(no_result) > 0):
                    print("no search result")
                    break

                if (len(no_result) == 0 and next_page is None):
                    print("one page search result found")
                    searches = html.xpath('//*[re:test(@id, "^[0-9]+$")]',
                                          namespaces={'re': "http://exslt.org/regular-expressions"})
                    # print(searches)
                    hrefs = map(ctls.find_url, searches)
                    searches = [x for x, y in zip(searches, hrefs) if y is not None]
                    # print(searches)

                    hrefs = filter(lambda x: not x is None, hrefs)
                    hrefs_org = map(ctls.real_url, hrefs)
                    # abstract = map(lambda x: ''.join(x.xpath('div[@class="c-abstract"]/text()')), searches)
                    print(hrefs_org)

                    url_hashmd5 = map(lambda x: hashlib.md5(x).hexdigest(), hrefs_org)

                    for ui in range(len(hrefs_org)):
                        print(url_hashmd5[ui])
                        print(unquote(kwords_i))
                        print(hrefs_org[ui])
                        db_manager.enqueue_crawl_url(url_hashmd5[ui], unquote(kwords_i),
                                                     url=hrefs_org[ui],
                                                     catorgy_url=catorgy_url,
                                                     kwords=unquote(kwords_i),
                                                     enque_time=time.strftime('%Y-%m-%d %H:%M:%S',
                                                                              time.localtime(time.time())),
                                                     update_time=time.strftime('%Y-%m-%d %H:%M:%S',
                                                                               time.localtime(time.time())),
                                                     status_crawl="new")
                    break

                if (next_page is not None):
                    print("more pages search result found")
                    searches = html.xpath('//*[re:test(@id, "^[0-9]+$")]',
                                          namespaces={'re': "http://exslt.org/regular-expressions"})
                    print(searches)
                    hrefs = map(ctls.find_url, searches)
                    print(hrefs)
                    searches = [x for x, y in zip(searches, hrefs) if y is not None]
                    print(searches)
                    hrefs = filter(lambda x: not x is None, hrefs)
                    hrefs_org = map(ctls.real_url, hrefs)
                    print(hrefs_org)
                    url_hashmd5 = map(lambda x: hashlib.md5(x).hexdigest(), hrefs_org)
                    print("url_hashmd5")
                    for ui in range(len(hrefs_org)):
                        print(url_hashmd5[ui])
                        print(unquote(kwords_i))
                        print(hrefs_org[ui])
                        db_manager.enqueue_crawl_url(url_hashmd5[ui], unquote(kwords_i),
                                                     url=hrefs_org[ui],
                                                     catorgy_url=catorgy_url,
                                                     kwords=unquote(kwords_i),
                                                     enque_time=time.strftime('%Y-%m-%d %H:%M:%S',
                                                                              time.localtime(time.time())),
                                                     update_time=time.strftime('%Y-%m-%d %H:%M:%S',
                                                                               time.localtime(time.time())),
                                                     status_crawl="new")
                    cur_url = next_page
                    next

    db_manager.finish_catorgy_url(c_url['id'])
