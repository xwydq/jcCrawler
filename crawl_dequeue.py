# -*- coding: utf-8 -*-
# import dbmanager
# https://github.com/Chyroc/WechatSogou
# 复制客户端的历史消息--浏览器--复制浏览器URL
from selenium import webdriver
import selenium
import os
from dbmanager import CrawlDatabaseManager
from lxml.html import clean
from crawl_tools import CrawlTools
from crawl_tools import ScrollStop
import subprocess


ctls = CrawlTools()
ctls.chdir_p()

scsp = ScrollStop()

db_manager = CrawlDatabaseManager(10)

grephant = "pgrep phantomjs"

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


## grep pid start phantomjs
try:
    phant_start = subprocess.check_output(grephant, shell=True)
    phant_start = phant_start.strip()
    phant_start = phant_start.split('\n')
except:
    phant_start = []
phant_start = set(phant_start)


# load PhantomJS driver
# driver = webdriver.PhantomJS(executable_path = '/usr/lib/node_modules/phantomjs-prebuilt/lib/phantom/bin/phantomjs',
#                              service_args=['--ignore-ssl-errors=true']) # set window size, better to fit the whole page in order to
driver = webdriver.PhantomJS(
    service_args=['--ignore-ssl-errors=true'])  # set window size, better to fit the whole page in order to
driver.set_window_size(1280, 2400)  # optional


## grep pid end phantomjs
try:
    phant_end = subprocess.check_output(grephant, shell=True)
    phant_end = phant_end.strip()
    phant_end = phant_end.split('\n')
except:
    phant_end = []
phant_end = set(phant_end)

phant_pid = phant_end - phant_start


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

            content = driver.page_source

            html_page = driver.page_source
            html_page = html_page.encode('utf-8')


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


## kill pid
for pi in phant_pid:
    os.system('kill -9 %s' % pi)
