# -*- coding: utf-8 -*-

import re
from datetime import datetime


class DateExtract:
    def __init__(self):
        self.patternList = ["(\d{4})([0|1]\d)([0-3]\d)", "(\d{4})(\d)([0-3]\d)", "(\d{4})(\d)(\d)",
                            "(\d{4})/([0|1]\d)/([0-3]\d)", "(\d{4})/(\d)/([0-3]\d)", "(\d{4})/(\d)/(\d)",
                            "(\d{4})-([0|1]\d)-([0-3]\d)", "(\d{4})-(\d)-([0-3]\d)", "(\d{4})-(\d)-(\d)"]

        self.patternList = map(lambda x: re.compile(x), self.patternList)
        self.dateNow = datetime.now().strftime('%Y-%m-%d')

    # str like '2017-01-01' to datetime class
    def str2date(self, s_date):
        try:
            g_date = datetime.strptime(s_date, '%Y-%m-%d')
        except:
            g_date = None
        return g_date

    def fittingDate(self, dateList):
        # [('2017', '11', '12'), ('2017', '09', '09')]==>'2017-09-09'
        dtFormat = map(lambda x: x[0] + "-" + "%02d" % int(x[1]) + "-" + "%02d" % int(x[2]), dateList)
        dtFormat = filter(lambda x: x <= self.dateNow, dtFormat)
        dtFormat = filter(lambda x: self.str2date(x), dtFormat)

        if len(dtFormat) > 0:
            return max(dtFormat)
        else:
            return None
            # re.findall(x, url_str)

    def extractUrlDate(self, url_str):
        m_str = map(lambda x: re.findall(x, url_str), self.patternList)
        # print(m_str)
        # print(m_str == None)
        m_str1 = filter(lambda x: x, m_str)
        m_str1 = map(lambda x: self.fittingDate(x), m_str1)
        # print(m_str1)
        if len(m_str1) > 0:
            m_date = max(m_str1)
            # m_str = m_str1[0]
            # m_date = m_str.group(1) + "-" + "%02d" % int(m_str.group(2)) + "-" + "%02d" % int(m_str.group(3))
        else:
            m_date = None
        # print(m_date)
        return m_date

        # example
        # url_str = "ashjdhsakldlasqu8932kasndka2017/09/23ashjd"
        # url_str = "ashjdhsakldla2017/11/23squ8932017/02/212kasndka2017/09/23ashjd"
        # url_str = "ashjdhsakld249/23ashjd"
        # from parseDate import DateExtract
        # det = DateExtract()
        # det.extractUrlDate(url_str)
