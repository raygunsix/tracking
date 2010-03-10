from fixture import DataSet

import datetime

d = datetime.datetime.now()

class PageviewsData(DataSet):
    class chrome:
        st_user_agent = "chrome"
        st_url = "test"
        st_spider_date = d
