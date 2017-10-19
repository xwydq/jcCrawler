# -*- coding: utf-8 -*-
# import dbmanager
# https://github.com/Chyroc/WechatSogou
# 复制客户端的历史消息--浏览器--复制浏览器URL

import os
import thread
import threading
import time
from dbmanager import CrawlDatabaseManager
import re
import datetime
from crawl_tools import CrawlTools
from crawl_tools import HtmlExtract
import os.path
import MySQLdb

from goose import Goose
from goose.text import StopWordsChinese

g = Goose({'stopwords_class': StopWordsChinese})

hext = HtmlExtract()

db_manager = CrawlDatabaseManager(10)

local_path = '/home/jc/crawlDir/'

filename = '7d1c64b7b99783920c4f23bc68a1539c'
filepath = local_path + filename + '/' + filename + '.html'

while True:
    # db_manager.init_extract_url()
    c_url = db_manager.dequeue_extract_url()
    print(c_url['url'])

    if c_url == None:
        break
    else:
        id = c_url['id']
        url = c_url['url']
        url_md5 = c_url['url_md5']
        catorgy_url = c_url['catorgy_url']

        extract_info = hext.url_extract(url_md5, catorgy_url, url)

        # extract_info = {
        #     'url_releasetime': None,
        #     'url_title': "asdkjh时间的'啊就是的",
        #     'url_content': "asdkjh时间的'啊'就是的",
        #     'ext_phrase': "as\"dkjh时\"间的'啊就是的",
        #     'ext_sentence': None,
        #     'pth_html': None
        # }

        for key, value in extract_info.items():
            if value is not None:
                extract_info[key] = MySQLdb.escape_string(value)

        # db_manager.update_url_info(1, extract_info)

        # print(extract_info)
        # print(type(extract_info))
        db_manager.update_url_info(id, extract_info)

        db_manager.finish_extract_url(id)
