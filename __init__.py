from fixture import DataSet

import datetime

d = datetime.datetime.now()

class PageviewData(DataSet):
    class pv_chrome:
        st_user_agent = "chrome"
        st_url = "test"
        st_spider_date = "2010-03-09 23:54:53.166829"

