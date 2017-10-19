# -*- coding: utf-8 -*-

from crawl_tools import HtmlExtract
import urllib2
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


wpth = '/home/jc/projectJC/crawler/back_conf/'
filename = 'exam'
filepath = wpth + filename + '/' + filename + '.html'

request_headers = {
    'connection': "keep-alive",
    'cache-control': "no-cache",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'accept-language': "zh-CN,en-US;q=0.8,en;q=0.6"
}


## clean text file
open(wpth + filename + '/' + 'url_releasetime', "w").close()
open(wpth + filename + '/' + 'url_title', "w").close()
open(wpth + filename + '/' + 'url_content', "w").close()


## download
request = urllib2.Request(cur_url, headers=request_headers)
response = urllib2.urlopen(request)
html_page = response.read()

fo = open(filepath, 'wb+')
fo.write(html_page)
fo.close()


## extract
hext = HtmlExtract()
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
