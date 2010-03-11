from fixture import DataSet

import datetime

now = datetime.datetime.now()
one_day = datetime.timedelta(days=1)

yesterday = now - one_day
weekago = now - (7 * one_day) 

class PageviewsData(DataSet):
    class pageview_google:
        st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
        st_url = "cookingresources.suite101.com/topiclist/article.cfm/ban_the_gut_bomb"
        st_spider_date = weekago
    class pageview_bing:
        st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
        st_url = "www.suite101.com/pages/reference.cfm/academie_internationale_du_vin"
        st_spider_date = yesterday
    class pageview_yahoo:
        st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
        st_url = "www.suite101.com/pages/reference.cfm/history_of_the_skyscraper"
        st_spider_date = now
