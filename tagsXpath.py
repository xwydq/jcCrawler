tags_xpath = {
    'www.huzhou.gov.cn':
        {
            'release_time': '/html/head/meta[@name="pubDate"]/@content',
            'url_title': '/html/head/title//text()',
            'url_content': '//*[@id="zoom"]//text()[not(ancestor::style)]'
        },
    'www.zunyi.gov.cn':
        {
            'release_time': '//div[@class="middle_biaoti"]//text() | '
                            '//div[@class="xxgk_dt_bd"]//text()',
            'url_title': '//div[@class="middle_title"]//text()',
            'url_content': '//div[@class="middlezhenwen clear"]//text()[not(ancestor::style)] | '
                           '//div[@class="xxgk_row"]//text()[not(ancestor::style)]'
        },
    'www.zjwy.gov.cn':
        {
            'release_time': '//*[@id="c"]//table/tbody/tr[3]//text()',
            'url_title': '//*[@id="c"]//table/tbody/tr[1]//text()',
            'url_content': '//*[@id="c"]//table/tbody/tr[4]//text()[not(ancestor::style)]'
        },
    'www.zjg.gov.cn':
        {
            'release_time': '//*[@id="wzabox"]//*[@class="main-date"]//text() | '
                            '//*[@id="ZwgkInfoDetail1_tblInfo"]/tbody/tr[1]//text()',
            'url_title': '//*[@id="wzabox"]//*[@class="main-h"]//text() | '
                         '//*[@id="ZwgkInfoDetail1_tblInfo"]/tbody/tr[2]//text()',
            'url_content': '//*[@id="wzabox"]//*[@class="main-block"]//text()[not(ancestor::style)] |'
                           '//*[@id="ZwgkInfoDetail1_tblInfo"]/tbody/tr[position()>2]//text()[not(ancestor::style)]'
        },
    'www.hangzhou.gov.cn':
        {
            'release_time': '//table[@width="90%"]/tbody/tr[2]//text()',
            'url_title': '//*[@id="barrierfree_container"]//*[@class="mdg_title"]//text()',
            'url_content': '//table[@width="90%"]/tbody//text()[not(ancestor::style)]'
        },
    'www.panan.gov.cn':
        {
            'release_time': '//div[@class="e_w95 pt20"]//text()',
            'url_title': '//div[@class="e_w95 pt10 pb20 content"]//*[@class="e_gLt8"]//text()',
            'url_content': '//div[@class="e_w95 pt10 pb20 content"]//text()[not(ancestor::style)]'
        },
    'www.suichang.gov.cn':
        {
            'release_time': '//div[@class="xl_doc"]//text() |'
                            '/html/body/table[4]/tbody/tr/td/table[2]//text() |'
                            '/html/body/table[4]/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr[6]//text()',
            'url_title': '//div[@class="xl_title"]//text() |'
                         '/html/body/table[4]/tbody/tr/td/table[1]//text() |'
                         '/html/body/table[4]/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr[2]//text()',
            'url_content': '//div[@class="xl_text"]//text()[not(ancestor::style)] |'
                           '/html/body/table[4]/tbody/tr[2]/td/table/tbody/tr/td/table[position()>1]//text()[not(ancestor::style)] |'
                           '/html/body/table[4]/tbody/tr/td/table[position()>1]//text()[not(ancestor::style)]'
        },
    'www.suqian.gov.cn':
        {
            'release_time': '//div[@style=" width:930px; margin:auto;"]//tbody/tr[2]//text() |'
                            '//div[@class="txttime txttime0"]/ul/li//text()',
            'url_title': '//*[@id="zoomtitle"]//text() |'
                         '//*[@id="zoomtitle"]//text()',
            'url_content': '//div[@style=" width:930px; margin:auto;"]//tbody/tr[position()>2]//text()[not(ancestor::style)] |'
                           '//*[@id="zoomcon"]//text()[not(ancestor::style)]'
        },
    'www.hbxq.gov.cn':
        {
            'release_time': '//td[@width="89"]//text()',
            'url_title': '//*[@id="zoomtitle"]//text()',
            'url_content': '//*[@id="zoomcon"]//text()[not(ancestor::style)]'
        },
    'www.mlnews.gov.cn':
        {
            'release_time': '//div[@class="atc hidden-xs"]/div[@align="center"]//text()',
            'url_title': '//div[@class="atc hidden-xs"]/h3//text()',
            'url_content': '//div[@class="atc hidden-xs"]//p//text()[not(ancestor::style)]'
        },
    'www.jsjt.gov.cn':
        {
            'release_time': '//font[@class="webfont"]//text() |'
                            '//*[@id="Zwgkdetail1_tr_comment"]//text()',
            'url_title': '//font[@style="font-size: 25px"]//text() |'
                         '//font[contains(@style,"font-size: 25px")]//text() |'
                         '//*[@id="Zwgkdetail1_tdTitle"]//text()',
            'url_content': '//*[@id="tblInfo"]/tbody/tr[position()>1]//text()[not(ancestor::style)] |'
                           '//td[@width="630"]//text()[not(ancestor::style)] |'
                           '//*[@id="Zwgkdetail1_spnContent"]//text()[not(ancestor::style)]'
        },
    'www.xuyi.gov.cn':
        {
            'release_time': '//td[@width="120"]//text()',
            'url_title': '//*[@id="printBody"]//h1[@class="aTitle"]//text()',
            'url_content': '//*[@id="printBody"]//text()[not(ancestor::style)]'
        },
    'www.nantong.gov.cn':
        {
            'release_time': '//*[@id="zw_time"]//text()',
            'url_title': '//*[@id="zw_title"]//text()',
            'url_content': '//*[@id="zw_content"]//text()[not(ancestor::style)]'
        },
    'www.miluo.gov.cn':
        {
            'release_time': '//div[@class="wznr_mess"]//text()',
            'url_title': '//h1[@class="content_title"]//text() |'
                         '//h2[@class="xxgk_view"]//text()',
            'url_content': '//*[@id="content_box"]//text()[not(ancestor::style)]'
        },
    'www.jiaxing.gov.cn':
        {
            'release_time': '//table[@class="collapse_table"]//text() |'
                            '//td[@class="gray_text12"]//text()',
            'url_title': '//td[@class="red_title20"]//text()',
            'url_content': '//table[@class="bk_gray"]//text()[not(ancestor::style)] |'
                           '//*[@id="text"]//text()[not(ancestor::style)]'
        },
    'www.anji.gov.cn':
        {
            'release_time': '//*[@class="link_7"]//text() |'
                            '//td[@class="mod_font08 mod_align link_26"]//text()',
            'url_title': '//*[@id="s3114938_content"]//font[@style="FONT-SIZE: 18px"]//text() |'
                         '//*[@id="s6056_content"]//td[@style="TEXT-ALIGN: center; HEIGHT: 40px; FONT-SIZE: 20px; VERTICAL-ALIGN: middle; FONT-WEIGHT: bold"]//text()',
            'url_content': '//*[@class="mod_box02"]//text()[not(ancestor::style)]'
        },
    'www.lyg.gov.cn':
        {
            'release_time': '//div[@class="art-menu"]//text()',
            'url_title': '//div[@class="art-title"]//text()',
            'url_content': '//*[@id="zoom"]//text()[not(ancestor::style)]'
        },
    'www.lishui.gov.cn':
        {
            'release_time': '//div[@class="xl_doc"]//text()',
            'url_title': '//div[@class="xl_title"]//text()',
            'url_content': '//div[@class="xl_text"]//text()[not(ancestor::style)]'
        },
    'www.quzhou.gov.cn':
        {
            'release_time': '/html/head/meta[@name="pubDate"]/@content | '
                            '/html/head/meta[@name="Maketime"]/@content',
            'url_title': '/html/head/meta[@name="title"]/@content',
            'url_content': '//*[@id="c"]//text()[not(ancestor::style)] | '
                           '//div[@class="main"]//text()[not(ancestor::style)]'
        },
    'www.huaian.gov.cn':
        {
            'release_time': '//div[@class="nr_k"]/h2//text() | '
                            '//div[@class="fx"]//text() | '
                            '//table[@width="97%"]/tbody/tr[2]//text()',
            'url_title': '//div[@class="nr_k"]/h1//text() | '
                         '//div[@class="artice"]/h1//text() | '
                         '//table[@width="97%"]/tbody/tr[1]//text()',
            'url_content': '//div[@class="nr_k"]/p//text()[not(ancestor::style)] | '
                           '//*[@id="zoom"]//text()[not(ancestor::style)] | '
                           '//table[@width="97%"]/tbody/tr[3]//text()[not(ancestor::style)]'
        },
    'www.xy.gov.cn':
        {
            'release_time': '//*[@id="PubinWebdate"]//text() | '
                            '//div[contains(@style,"font-size: 12px")]//text()',
            'url_title': '//*[@id="Title"]//text() | '
                         '//font[@class="InfoTitle"]//text()',
            'url_content': '//*[@id="InfoContent"]//text()[not(ancestor::style)] | '
                           '//*[@id="TDContent"]//text()[not(ancestor::style)]'
        },
    'www.anshun.gov.cn':
        {
            'release_time': '//div[@class="toolbar"]//text()',
            'url_title': '//div[@class="title"]/h1//text()',
            'url_content': '//div[@class="content"]//text()[not(ancestor::style)]'
        },
    'www.xixiu.gov.cn':
        {
            'release_time': '//div[@class="toolbar"]//text()',
            'url_title': '//div[@class="title"]/h1//text()',
            'url_content': '//div[@class="content"]//text()[not(ancestor::style)]'
        },
    'www.yancheng.gov.cn':
        {
            'release_time': '//td[@height="24"]//text() | '
                            '//*[@id="container"]/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[2]/td//text() | '
                            '/html/body/table[1]/tbody/tr/td/table[2]/tbody/tr[2]/td/table//text()',
            'url_title': '//td[@height="40"]//text() | '
                         '//*[@id="container"]/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[1]/td/em//text() | '
                         '/html/body/table[1]/tbody/tr/td/table[3]/tbody/tr[2]/td/table[1]//text()',
            'url_content': '//div[@class="cas_content"]//text()[not(ancestor::style)] | '
                           '//*[@id="container"]/table[1]/tbody/tr/td[1]/table[3]//text()[not(ancestor::style)] | '
                           '/html/body/table[1]/tbody/tr/td/table[3]/tbody/tr[2]/td/table[1]/tbody/tr[1]/td//text()[not(ancestor::style)] | '
                           '/html/body/table[1]/tbody/tr/td/table[3]/tbody/tr[2]/td/table[2]//text()[not(ancestor::style)]'
        },
    'www.junshan.gov.cn':
        {
            'release_time': '//div[@class="articleCon"]//div[@class="property"]//text() | '
                            '//div[@id="DataCont"]//text()',
            'url_title': '//div[@class="articleCon"]//*[@class="articleTitle"]//text() | '
                         '//div[@id="content"]//h3[@class="title"]//text()',
            'url_content': '//div[@class="articleCon"]//div[@class="conTxt"]//text()[not(ancestor::style)] | '
                           '//div[@id="fontzoom"]//text()[not(ancestor::style)]'
        },
    'www.yueyang.gov.cn':
        {
            'release_time': '/html/body/div[2]/table[2]/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr/td//text() | '
                            '//div[@class="my_links ovf"]//text() | '
                            '//div[@class="wznr_mess"]//text() | '
                            '//div[@class="author"]//text() |'
                            '//div[@id="new_cont"]//div[@class="date"]//text()',
            'url_title': '/html/body/div[2]/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td/strong//text() | '
                         '//div[@class="article_Title"]//text() | '
                         '//h1[@class="content_title"]//text() | '
                         '//div[@class="BoxCont clearfix"]/h2//text() |'
                         '//div[@id="new_cont"]/h2//text()',
            'url_content': '/html/body/div[2]/table[2]/tbody/tr[2]/td/table/tbody/tr[5]//text()[not(ancestor::style)] | '
                           '//div[@class="bg_ejym_12 back_white"]//div[@class="content"]//text()[not(ancestor::style)] | '
                           '//div[@id="content_box"]//text()[not(ancestor::style)] | '
                           '//div[@id="content"]//text()[not(ancestor::style)]'
        },
    'www.zjjyd.gov.cn':
        {
            'release_time': '//div[@class="section"]//div[@class="info"]//text()',
            'url_title': '//div[@class="section"]/h2//text()',
            'url_content': '//div[@class="section"]//div[@class="art_main"]//text()'
        },
    'www.zjj.gov.cn':
        {
            'release_time': '//p[@class="note"]//text() | '
                            '//div[@class="xxgktop"]//text()',
            'url_title': '//div[@class="maincontainer"]//div/h2/voice//text() | '
                         '//div[@class="maincontainer"]/div/div/voice//text()',
            'url_content': '//div[@id="zoom"]//text()[not(ancestor::style)] | '
                           '//div[@class="content"]//text()[not(ancestor::style)]'
        },
    'www.gysqz.gov.cn':
        {
            'release_time': '//div[@class="wzbjxx"]//text()',
            'url_title': '//div[@class="wztit"]//text()',
            'url_content': '//div[@class="wzcon"]//text()[not(ancestor::style)]'
        },
    'epaper.gytoday.cn':
        {
            'release_time': '/html/body/table[1]/tbody/tr[2]/td[2]/table[1]/tbody/tr/td[1]/span/strong[1]//text()',
            'url_title': '//founder-title//text()',
            'url_content': '/html/body/table[1]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/div/table//text()[not(ancestor::style)]'
        },
    'www.jiyuan.gov.cn':
        {
            'release_time': '//div[@class="detail-container"]//div[@class="son-title"]//text()',
            'url_title': '//div[@class="detail-container"]//div[@class="title"]//text()[not(ancestor::style)]',
            'url_content': '//div[@class="detail-container"]//div[@class="detail"]//div[@class="TRS_Editor"]//text()[not(ancestor::style)]'
        },
    'www.henan.gov.cn':
        {
            'release_time': '//td[@bgcolor="#E7E7E7"]//text()',
            'url_title': '//div[@class="title"]//text()[not(ancestor::style)]',
            'url_content': '//td[@class="content"]//text()[not(ancestor::style)]'
        },
    'www.haining.gov.cn':
        {
            'release_time': '//*[@id="from"]//text()',
            'url_title': '//*[@id="title_con"]//text()[not(ancestor::style)]',
            'url_content': '//*[@id="content_xiangxi"]//text()[not(ancestor::style)]'
        },
    'www.changsha.gov.cn':
        {
            'release_time': '//ul[@class="docFunc"]//text() | '
                            '//ul[@class="ul_docInfo"]//text()',
            'url_title': '//h1[@class="docTitle"]//text()[not(ancestor::style)] | '
                         '//li[@class="li_docTitle"]//text()[not(ancestor::style)]',
            'url_content': '//*[@id="docContent_detail"]//text()[not(ancestor::style)]'
        },
    'www.qidong.gov.cn':
        {
            'release_time': '//div[@class="act_m"]//div[@class="cbo"]//text()',
            'url_title': '//div[@class="act_m"]/h1//text()[not(ancestor::style)]',
            'url_content': '//*[@id="zoom"]//text()[not(ancestor::style)]'
        },
    'changde.gov.cn':
        {
            'release_time': '/html/head/meta[@name="pubDate"]/@content',
            'url_title': '/html/head/meta[@name="title"]/@content',
            'url_content': '//*[@id="zoom"]//text()[not(ancestor::style)]'
        },
    'www.taoyuan.gov.cn':
        {
            'release_time': '//*[@class="articleCon"]//div[@class="property"]//text()',
            'url_title': '//*[@class="articleCon"]//*[@class="title"]//text()[not(ancestor::style)]',
            'url_content': '//*[@class="articleCon"]//div[@class="conTxt"]//text()[not(ancestor::style)]'
        },
    'www.ahmg.gov.cn':
        {
            'release_time': '//*[@id="color_printsssss"]//div[@class="newsinfo"]//text() | '
                            '//div[@class="fbh_info"]//text()',
            'url_title': '//*[@id="color_printsssss"]//*[@class="newstitle"]//text()[not(ancestor::style)] | '
                         '//div[@class="fbhbox1l fl"]/h1//text()[not(ancestor::style)]',
            'url_content': '//div[@id="J_content"]//text()[not(ancestor::style)] | '
                           '//div[@class="fbh_js"]//text()[not(ancestor::style)]'
        },
    'www.cixi.gov.cn':
        {
            'release_time': '/html/head/meta[@name="pubDate"]/@content',
            'url_title': '/html/head/meta[@name="title"]/@content',
            'url_content': '//*[@id="zoom"]//text()[not(ancestor::style)]'
        },
    'www.wuxi.gov.cn':
        {
            'release_time': '//*[@id="sch_box"]/p[@class="explain"]//text() |'
                            '//div[@class="mainCont"]/p[@class="explain"]//text()',
            'url_title': '//*[@id="sch_box"]/h1//text()[not(ancestor::style)] |'
                         '//div[@class="mainCont"]/h1//text()[not(ancestor::style)]',
            'url_content': '//div[@class="Zoom"]//text()[not(ancestor::style)]'
        },
    'www.zjtz.gov.cn':
        {
            'release_time': '/html/body/table[3]/tbody/tr/td/table[1]/tbody/tr/td//text()',
            'url_title': '//*[@id="title"]//text()[not(ancestor::style)]',
            'url_content': '//*[@id="zoom"]//text()[not(ancestor::style)] |'
                           '//div[@class="TRS_Editor"]//text()[not(ancestor::style)]'
        },
    'www.nbhz.gov.cn':
        {
            'release_time': '//*[@id="ctl00_ContentPlaceHolder6_lblAddedDate"]//text()',
            'url_title': '//*[@id="ctl00_ContentPlaceHolder6_lblTitle"]//text()[not(ancestor::style)]',
            'url_content': '//*[@id="ctl00_ContentPlaceHolder6_lblText"]//text()[not(ancestor::style)]'
        },
    'www.changzhou.gov.cn':
        {
            'release_time': '//td[./span[@id="source"]]//text() | '
                            '/html/body/table[6]/tbody/tr[2]/td/table[2]//text() | '
                            '/html/body/table[3]/tbody/tr/td/table[3]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/strong//text()',
            'url_title': '//td[@class="NewsTitle"]//text()[not(ancestor::style)] | '
                         '/html/body/table[6]/tbody/tr[2]/td/table[2]/tbody/tr[1]/td/span[2]//text()[not(ancestor::style)] | '
                         '/html/body/table[3]/tbody/tr/td/table[3]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/strong/a//text()[not(ancestor::style)]',
            'url_content': '//*[@id="czfxfontzoom"]//text()[not(ancestor::style)] | '
                           '/html/body/table[6]/tbody/tr[2]/td/table[position()>3]//text()[not(ancestor::style)] | '
                           '/html/body/table[3]/tbody/tr/td/table[3]/tbody/tr/td/table//text()[not(ancestor::style)]'
        },
    'www.yixing.gov.cn':
        {
            'release_time': '//div[@class="g_show_rq"]//text() | '
                            '//div[@class="show_author"]//text() | '
                            '//div[@class="content_tir"]//text() | '
                            '//span[@class="sj"]//text() | '
                            '//td[@class="mod_font08_t mod_padding5l mod_padding5r"]//text() | '
                            '//div[@class="jmyg_r"]//text()',
            'url_title': '//div[@class="g_show_title"]//text()[not(ancestor::style)] | '
                         '//div[@class="show_title"]//text()[not(ancestor::style)] | '
                         '//div[@class="content_sec"]//text()[not(ancestor::style)] | '
                         '//span[@class="dbt"]//text()[not(ancestor::style)] | '
                         '//*[@id="s430349_content"]/table/tbody/tr[1]/td/font//text()[not(ancestor::style)]',
            'url_content': '//div[@class="g_show_article"]//text()[not(ancestor::style)] | '
                           '//div[@class="show_content"]//text()[not(ancestor::style)] | '
                           '//div[@class="content"]//text()[not(ancestor::style)] | '
                           '//*[@id="article_content"]//text()[not(ancestor::style)] | '
                           '//div[@class="ftsl_content"]//text()[not(ancestor::style)]'
        },
    'www.suzhou.gov.cn':
        {
            'release_time': '//*[@id="text-content"]/dl/dd[1]//text() | '
                            '//div[@class="con2 clearfix"]/h4//text()',
            'url_title': '//*[@id="text-content"]/dl/dt//text()[not(ancestor::style)] | '
                         '//div[@class="con2 clearfix"]/h1//text()[not(ancestor::style)]',
            'url_content': '//*[@id="con_color"]//text()[not(ancestor::style)] | '
                           '//div[@class="cbank clearfix"]//text()[not(ancestor::style)]'
        },
    'www.zjjnews.cn':
        {
            'release_time': '//*[@id="article"]/p//text() | '
                            '//*[@id="list_news"]/small//text()',
            'url_title': '//*[@id="article"]/h1//text()[not(ancestor::style)] | '
                         '//*[@id="list_news"]/h1//text()[not(ancestor::style)]',
            'url_content': '//*[@id="article"]/div//text()[not(ancestor::style)] | '
                           '//*[@id="list_news"]/ul//text()[not(ancestor::style)]'
        },
    'news.163.com':
        {
            'release_time': '//*[@id="epContentLeft"]/div[@class="post_time_source"]//text()',
            'url_title': '//*[@id="epContentLeft"]/h1//text()[not(ancestor::style)]',
            'url_content': '//*[@id="endText"]//text()[not(ancestor::style)]'
        },
    'qq.com':
        {
            'release_time': '//div[@class="qq_bar clearfix"]//text() |'
                            '//div[@class="tit-bar clearfix"]//text()',
            'url_title': '//div[@class="hd"]/h1//text()[not(ancestor::style)]',
            'url_content': '//*[@id="Cnt-Main-Article-QQ"]//text()[not(ancestor::style)]'
        },
    'www.sohu.com':
        {
            'release_time': '//div[@class="article-info"]//text()',
            'url_title': '//div[@class="text-title"]/h1//text()[not(ancestor::style)]',
            'url_content': '//article[@class="article"]//text()[not(ancestor::style)]'
        },
    'hnrb.voc.com.cn':
        {
            'release_time': '//div[@class="from"]//text() |'
                            '/html/body/table/tbody/tr[1]/td[2]/table[1]/tbody/tr[3]/td[1]/span/strong//text()',
            'url_title': '//div[@class="bigtitle"]//text()[not(ancestor::style)] |'
                         '/html/body/table/tbody/tr[1]/td[2]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td/table/tbody/tr[2]/td//text()[not(ancestor::style)]',
            'url_content': '//*[@id="zoom"]//text()[not(ancestor::style)] |'
                           '//*[@id="ozoom"]//text()[not(ancestor::style)]'
        },
    'www.803.com.cn':
        {
            'release_time': '//div[@class="news_info"]//text()',
            'url_title': '//div[@class="news_title"]//text()[not(ancestor::style)]',
            'url_content': '//div[@class="content"]//text()[not(ancestor::style)]'
        },
    'news.cqwb.com.cn':
        {
            'release_time': '//div[@class="news_content mb25"]/h3//text() | '
                            '//div[@class="articleInfo"]//text()',
            'url_title': '//div[@class="news_content mb25"]/h1//text()[not(ancestor::style)] | '
                         '//div[@class="content_hd"]/h1//text()[not(ancestor::style)]',
            'url_content': '//div[@class="news_content_text"]//text()[not(ancestor::style)] | '
                           '//div[@class="content"]//text()[not(ancestor::style)]'
        },
    'www.cn139.cn':
        {
            'release_time': '//div[@class="resource"]//text()',
            'url_title': '//div[@class="title"]//text()[not(ancestor::style)]',
            'url_content': '//div[@class="content"]//text()[not(ancestor::style)]'
        },
    'www.jhwb.com.cn':
        {
            'release_time': '//p[@class="time"]//text()',
            'url_title': '//div[@class="kleft detail"]/h1//text()[not(ancestor::style)]',
            'url_content': '//div[@class="kleft detail"]/p[position()>1]//text()[not(ancestor::style)]'
        },
    'finance.sina.com.cn':
        {
            'release_time': '//*[@id="pub_date"]//text() |'
                            '//div[@class="page-info"]//text()',
            'url_title': '//*[@id="artibodyTitle"]//text()[not(ancestor::style)]',
            'url_content': '//*[@id="artibody"]//text()[not(ancestor::style)]'
        },
    'www.bidcenter.com.cn':
        {
            'release_time': '//div[@class="shareL fl"]//text()',
            'url_title': '//h1[@class="item-tit"]//text()[not(ancestor::style)]',
            'url_content': '//div[@class="main-left fl"]//text()[not(ancestor::style)]'
        },
    'www.zjjrtv.com':
        {
            'release_time': '//div[@class="fleft"]//text()',
            'url_title': '//div[@class="readheader"]/div/h1//text()[not(ancestor::style)]',
            'url_content': '//*[@id="readtext"]//text()[not(ancestor::style)]'
        },
    'news.ifeng.com':
        {
            'release_time': '//div[@class="p_time"]//text()',
            'url_title': '//*[@id="artical_topic"]//text()[not(ancestor::style)]',
            'url_content': '//*[@id="main_content"]//text()[not(ancestor::style)]'
        },
    'news.xhby.net':
        {
            'release_time': '//*[@id="content-source"]//text() |'
                            '//*[@id="pubtime_baidu"]//text()',
            'url_title': '//*[@id="content-title"]//text()[not(ancestor::style)] |'
                         '//*[@id="title"]//text()[not(ancestor::style)]',
            'url_content': '//*[@id="content-text"]//text()[not(ancestor::style)] |'
                           '//*[@id="content"]//text()[not(ancestor::style)]'
        },
    'hn.rednet.cn':
        {
            'release_time': '//*[@id="pubtime_baidu"]//text() |'
                            '//span[@class="pubdate"]//text()',
            'url_title': '//*[@id="artilcetitle"]/h1//text()[not(ancestor::style)]',
            'url_content': '//*[@id="articlecontent"]//text()[not(ancestor::style)]'
        },
    'zhaobiao.wubaiyi.com':
        {
            'release_time': '//*[@id="Article"]/h1//span//text()[not(ancestor::style)]',
            'url_title': '//*[@id="Article"]/h1//text()[not(ancestor::span)]',
            'url_content': '//div[@class="content"]//text()[not(ancestor::style)]'
        },
    'kuaizhan.com':
        {
            'release_time': '//div[contains(@class,"mod-article-attr")]//text()',
            'url_title': '//div[contains(@class,"mod-title")]//text()[not(ancestor::span)]',
            'url_content': '//div[contains(@class,"article-content")]//text()[not(ancestor::style)]'
        },
    'www.hnkfq.com.cn':
        {
            'release_time': '//div[@class="rqttie"]//text()',
            'url_title': '//div[@class="biaot"]//text()[not(ancestor::span)]',
            'url_content': '//div[@class="newxxjs"]//text()[not(ancestor::style)]'
        },
    'bbs.211600.com':
        {
            'release_time': '//div[@class="postaaa posta0"]//div[@class="authi"]//text()',
            'url_title': '//*[@id="thread_subject"]//text()[not(ancestor::style)]',
            'url_content': '//div[@class="pcb"]//text()[not(ancestor::style)]'
        },
    'www.ccpithz.org':
        {
            'release_time': '//h1[@class="contentheader"]//text()',
            'url_title': '//h1[@class="contentheader"]//text()[not(ancestor::style)]',
            'url_content': '//div[@class="contents"]//text()[not(ancestor::style)]'
        },
    'www.jiangjiangda.com':
        {
            'release_time': '//div[@class="article-header"]/div[@class="info"]//text()',
            'url_title': '//div[@class="article-header"]/h1[@class="title"]//text()[not(ancestor::style)]',
            'url_content': '//*[@id="main-content"]//text()[not(ancestor::style)]'
        },
    'js.ifeng.com':
        {
            'release_time': '//*[@id="artical_sth"]//text()',
            'url_title': '//*[@id="artical_topic"]//text()[not(ancestor::style)]',
            'url_content': '//*[@id="artical_real"]//text()[not(ancestor::style)]'
        },
    'www.wxbh.gov.cn':
        {
            'release_time': '//div[@class="lst-10"]//text() | '
                            '//div[@class="wz-time"]//text() | '
                            '//div[@class="art_time"]//text() | '
                            '//div[@class="ind-58"]//text() | '
                            '//div[@class="ind-54"]//text() | '
                            '//div[@class="article_post"]//text() | '
                            '//div[@class="time"]//text()',
            'url_title': '//div[@class="lw_title"]//text()[not(ancestor::style)]',
            'url_content': '//div[@class="lw_content"]//text()[not(ancestor::style)] | '
                           '//div[@class="wz-main"]//text()[not(ancestor::style)] | '
                           '//div[@class="art_content"]//text()[not(ancestor::style)]'
        },
    'zjnews.china.com.cn':
        {
            'release_time': '//ul[@class="article-meta"]//text()',
            'url_title': '//h1[@class="article-title"]//text()[not(ancestor::style)]',
            'url_content': '//article[@class="article-content"]//text()[not(ancestor::style)]'
        },
    'www.gaoloumi.com':
        {
            'release_time': '//div[@class="authi"]//text()',
            'url_title': '//*[@id="thread_subject"]//text()[not(ancestor::style)]',
            'url_content': '//div[@class="t_fsz"]//text()[not(ancestor::style)]'
        },
    'ttnews.zjol.com.cn':
        {
            'release_time': '//td[@height="36"]//text()',
            'url_title': '//*[@id="thistitle"]//text()[not(ancestor::style)]',
            'url_content': '//*[@id="oZoom"]//text()[not(ancestor::style)]'
        },
    'info.meadin.com':
        {
            'release_time': '//p[@class="source"]//text() |'
                            '//div[@class="information"]//text()',
            'url_title': '//h1[@class="article-title"]//text()[not(ancestor::style)] |'
                         '//div[@class="top"]/h1//text()[not(ancestor::style)]',
            'url_content': '//div[@class="article js-article"]//text()[not(ancestor::style)] |'
                           '//div[@class="introduction"]//text()[not(ancestor::style)] |'
                           '//*[@id="news-content"]//text()[not(ancestor::style)]'
        },
    'www.xiangshan.gov.cn':
        {
            'release_time': '//*[@id="article"]/tbody/tr[2]/td/table/tbody/tr[1]/td/span[1]//text()',
            'url_title': '//td[@class="title"]//text()[not(ancestor::style)]',
            'url_content': '//*[@id="zoom"]//text()[not(ancestor::style)]'
        },
    'tsxz.zjol.com.cn':
        {
            'release_time': '//*[@id="pubtime_baidu"]//text()',
            'url_title': '//h1[@class="artTitle"]//text()[not(ancestor::style)]',
            'url_content': '//div[@class="artCon"]//text()[not(ancestor::style)]'
        },
    'www.prnasia.com':
        {
            'release_time': '//div[@id="header-message"]//span[@class="timestamp"]//text() |'
                            '//div[@class="entry-meta"]//text()',
            'url_title': '//*[@id="header-message"]/h2//text()[not(ancestor::style)] |'
                         '//*[@id="contenttitle"]//text()[not(ancestor::style)] |'
                         '//div[@class="entry-title"]//text()[not(ancestor::style)]',
            'url_content': '//*[@id="dvContent"]//text()[not(ancestor::style)] |'
                           '//div[@class="entry-content"]//text()[not(ancestor::style)]'
        }

}

import pandas as pd
import mysql.connector as sql

df_xpath = pd.DataFrame(tags_xpath)
df_xpath = df_xpath.T

db_connection = sql.connect(host='172.16.0.116', database='jc_crawl', user='root', password='jcplanb.com')
# db_cursor = db_connection.cursor()
df = pd.read_sql('SELECT * FROM crawl_catorgy', con=db_connection)
df_xpath.to_sql(name='tags_xpath', con=db_connection, if_exists='replace', flavor='mysql')

df_xpath.to_csv('tags_xpath.csv')
