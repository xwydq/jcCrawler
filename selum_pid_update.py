# -*- coding: utf-8 -*-

## 找到启动phantomjs时对应 的进程pid
## 在推出程序时kill对应pid

from selenium import webdriver
from lxml.html import clean
from crawl_tools import CrawlTools
from crawl_tools import ScrollStop
import time
from crawl_tools import HtmlExtract
import os
# import MySQLdb
import subprocess

ISOTIMEFORMAT = '%Y-%m-%d %X'
batcmd = "pgrep phantomjs"

ctls = CrawlTools()
# ctls.chdir_p()
scsp = ScrollStop()

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

print(time.strftime(ISOTIMEFORMAT, time.localtime()))
try:
    result1 = subprocess.check_output(batcmd, shell=True)
    result1 = result1.strip()
    result1 = result1.split('\n')
except:
    result1 = []
result1 = set(result1)
print(type(result1))
print(result1)
print('---------')

driver = webdriver.PhantomJS(
    service_args=['--ignore-ssl-errors=true'])  # set window size, better to fit the whole page in order to
driver.set_window_size(1280, 2400)  # optional

print(time.strftime(ISOTIMEFORMAT, time.localtime()))

# os.system('pgrep phantomjs')
try:
    result2 = subprocess.check_output(batcmd, shell=True)
    result2 = result2.strip()
    result2 = result2.split('\n')
except:
    result2 = []
result2 = set(result2)
print(type(result2))
print(result2)

setDiv = result2 - result1
print(type(setDiv))
print(setDiv)

for i in setDiv:
    print('kill -9 %s' % i)
    os.system('kill -9 %s' % i)

try:
    result2 = subprocess.check_output(batcmd, shell=True)
    result2 = result2.strip()
    result2 = result2.split('\n')
except:
    result2 = []
result2 = set(result2)
print(type(result2))
print(result2)

setDiv = result2 - result1
print(type(setDiv))
print(setDiv)



# ##############
# result1 = []
# result1 = set(result1)
# result2 = []
# result2 = set(result2)
#
# setDiv = result2 - result1
# print(type(setDiv))
# print(setDiv)
#
#
# for i in setDiv:
#     print('kill -9 %s' % i)
#     os.system('kill -9 %s' % i)
