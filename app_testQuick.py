# -*- coding: utf-8 -*-
from selenium import webdriver
from lxml.html import clean
from crawl_tools import CrawlTools
from crawl_tools import ScrollStop
from crawl_tools import HtmlExtract
import os
import subprocess
import sys

###
catorgy_url = sys.argv[1]
cur_url = sys.argv[2]
# print(catorgy_url)
# print(cur_url)
###

###
# cur_url = 'http://www.huaian.gov.cn/xwzx/qxkx/content/5e38cfba5cb05b77015cd3e2cd9c4a3a.html'
# catorgy_url = 'www.huaian.gov.cn'
###


ctls = CrawlTools()
scsp = ScrollStop()
hext = HtmlExtract()

wpth = '/home/jc/projectJC/crawler/back_conf/'
filename = 'exam'
filepath = wpth + filename + '/' + filename + '.html'
pause = 5.5
grephant = "pgrep phantomjs"

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


## clean
open(wpth + filename + '/' + 'url_releasetime', "w").close()
open(wpth + filename + '/' + 'url_title', "w").close()
open(wpth + filename + '/' + 'url_content', "w").close()


## download html
driver.get(cur_url)
scsp.stop_scroll(driver, catorgy_url)

content = driver.page_source
html_page = driver.page_source
html_page = html_page.encode('utf-8')

fo = open(filepath, 'wb+')
fo.write(html_page)
fo.close()



## extract
hext.FPATH = wpth
extract_info = hext.url_extract(filename, catorgy_url, cur_url)

## insert text info
for key, value in extract_info.items():
    if value is not None:
        print(key)
        print(extract_info[key])
        text_file = open(wpth + filename + '/' + key, "w")
        text_file.write(extract_info[key])
        text_file.close()


## kill pid
for pi in phant_pid:
    os.system('kill -9 %s' % pi)
