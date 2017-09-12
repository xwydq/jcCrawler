# -*- coding: utf-8 -*-
# import dbmanager
# https://github.com/Chyroc/WechatSogou
# 复制客户端的历史消息--浏览器--复制浏览器URL
from selenium import webdriver
import time
from lxml import etree

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

# load PhantomJS driver
# driver = webdriver.PhantomJS(executable_path = '/usr/lib/node_modules/phantomjs-prebuilt/lib/phantom/bin/phantomjs',
#                              service_args=['--ignore-ssl-errors=true']) # set window size, better to fit the whole page in order to
driver = webdriver.PhantomJS(
    service_args=['--ignore-ssl-errors=true'])  # set window size, better to fit the whole page in order to
driver.set_window_size(1280, 2000)  # optional

cur_url = 'http://www.sohu.com/a/163042044_447403'
driver.get(cur_url)

lastHeight = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(pause)
    newHeight = driver.execute_script("return document.body.scrollHeight")
    print(newHeight)

    html_page = driver.page_source
    html_page = html_page.encode('utf-8')
    html = etree.HTML(html_page)

    testTag = html.xpath(u'//*[@class="article-oper"]//text()')
    testTag = ''.join(testTag)

    if newHeight == lastHeight or lastHeight > 20000 or testTag <> '':
        break
    lastHeight = newHeight

content = driver.page_source

file_png = "test.png"

# save png
driver.save_screenshot(file_png)
