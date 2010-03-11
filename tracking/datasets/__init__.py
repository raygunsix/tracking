from fixture import DataSet

import datetime

d = datetime.datetime.now()

class PageviewsData(DataSet):
    class pageview_google:
        st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
        st_url = "cookingresources.suite101.com/topiclist/article.cfm/ban_the_gut_bomb"
        st_spider_date = d
    class pageview_bing:
        st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
        st_url = "www.suite101.com/pages/reference.cfm/academie_internationale_du_vin"
        st_spider_date = d
    class pageview_yahoo:
        st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
        st_url = "www.suite101.com/pages/reference.cfm/history_of_the_skyscraper"
        st_spider_date = d
