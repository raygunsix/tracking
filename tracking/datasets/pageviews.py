import datetime

from fixture import DataSet


# This function is a workaround to support parsing microseconds on python 2.5
# which is the default on Mac OS X Leopard
# stackoverflow.com/questions/531157/parsing-datetime-strings-with-microseconds
def str2datetime(s):
    parts = s.split('.')
    dt = datetime.datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S")
    return dt.replace(microsecond=int(parts[1]))

class PageviewsData(DataSet):

    class pv1:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/reference.cfm/tumbledown"
           st_spider_date = str2datetime("2010-02-24 18:04:35.263243")
    
    class pv2:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "nonprofitfundraising.suite101.com/topiclist/article.cfm/successful_fundraiser_dinners"
           st_spider_date = str2datetime("2010-02-24 18:04:38.770709")
    
    class pv3:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "student-loans.suite101.com/topiclist/article.cfm/south_carolina_student_loan"
           st_spider_date = str2datetime("2010-02-24 18:04:40.408362")
    
    class pv4:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/301/discussion.cfm/tolkien/71217/1-6"
           st_spider_date = str2datetime("2010-02-24 18:04:40.473019")
    
    class pv5:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "www.suite101.com/301/discussion.cfm/camping/6152/335768"
           st_spider_date = str2datetime("2010-02-24 18:04:41.097824")
    
    class pv6:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/reference.cfm/ceti"
           st_spider_date = str2datetime("2010-02-24 18:04:41.990463")
    
    class pv7:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/messianic_judaism/109321"
           st_spider_date = str2datetime("2010-02-24 18:04:47.059333")
    
    class pv8:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/math_fun/80825"
           st_spider_date = str2datetime("2010-02-24 18:04:50.663197")
    
    class pv9:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/artists_retired/20458/1"
           st_spider_date = str2datetime("2010-02-24 18:04:53.389698")
    
    class pv10:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/daffodils/59197/2"
           st_spider_date = str2datetime("2010-02-24 18:04:54.225587")
    
    class pv11:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/herbalism/60360/4"
           st_spider_date = str2datetime("2010-02-24 18:05:01.404367")
    
    class pv12:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "www.suite101.com/pages/reference.cfm/two_tracks_of_salvation"
           st_spider_date = str2datetime("2010-02-24 18:05:05.110349")
    
    class pv13:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/wolves_retired/33307/1"
           st_spider_date = str2datetime("2010-02-24 18:05:07.532933")
    
    class pv14:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/article_old.cfm/circus_circus/65161"
           st_spider_date = str2datetime("2010-02-24 18:05:10.646532")
    
    class pv15:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/article_old.cfm/build_your_own_website/107097"
           st_spider_date = str2datetime("2010-02-24 18:05:10.928332")
    
    class pv16:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/premature_babies/37268/1"
           st_spider_date = str2datetime("2010-02-24 18:05:12.709799")
    
    class pv17:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "historicalmethodology.suite101.com/topiclist/article.cfm/diaries-and-historical-research"
           st_spider_date = str2datetime("2010-02-24 18:05:13.729951")
    
    class pv18:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "mortgage-negotiation.suite101.com/topiclist/article.cfm/the_making_home_affordable_refinance_program"
           st_spider_date = str2datetime("2010-02-24 18:05:14.565008")
    
    class pv19:
           st_user_agent = "samsung-sgh-e250/1.0 profile/midp-2.0 configuration/cldc-1.1 up.browser/6.2.3.3.c.1.101 (gui) mmp/2.0 (compatible; googlebot-mobile/2.1; +http://www.google.com/bot.html)"
           st_url = "spring-recipes.suite101.com/topiclist/article.cfm/easter_appetizers"
           st_spider_date = str2datetime("2010-02-24 18:05:15.369409")
    
    class pv20:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/family_historians/81493/1"
           st_spider_date = str2datetime("2010-02-24 18:05:21.79352")
    
    class pv21:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "www.suite101.com/pages/reference.cfm/dispatch_programs"
           st_spider_date = str2datetime("2010-02-24 18:05:23.544162")
    
    class pv22:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/teaching_theatre/92758/1"
           st_spider_date = str2datetime("2010-02-24 18:05:24.820342")
    
    class pv23:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/reference.cfm/lettuce_wrap_recipes"
           st_spider_date = str2datetime("2010-02-24 18:05:29.854074")
    
    class pv24:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/reference.cfm/sociology_looking_glass_self"
           st_spider_date = str2datetime("2010-02-24 18:05:32.763964")
    
    class pv25:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "www.suite101.com/pages/reference.cfm/bad_credit_home_buyers"
           st_spider_date = str2datetime("2010-02-24 18:05:33.719617")
    
    class pv26:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "filmtvindustry.suite101.com/topiclist/article.cfm/the_oscar_waiting_game"
           st_spider_date = str2datetime("2010-02-24 18:05:35.742251")
    
    class pv27:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "www.suite101.com/pages/reference.cfm/lorenzen"
           st_spider_date = str2datetime("2010-02-24 18:05:35.986865")
    
    class pv28:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/women_painters/109682"
           st_spider_date = str2datetime("2010-02-24 18:05:37.105984")
    
    class pv29:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "architecture.suite101.com/topiclist/article.cfm/barbie-the-architect"
           st_spider_date = str2datetime("2010-02-24 18:05:37.648031")
    
    class pv30:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "www.suite101.com/pages/reference.cfm/slow_play"
           st_spider_date = str2datetime("2010-02-24 18:05:38.69686")
    
    class pv31:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/diversity/20496/1"
           st_spider_date = str2datetime("2010-02-24 18:05:39.286009")
    
    class pv32:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/reference.cfm/pairc_windfarm"
           st_spider_date = str2datetime("2010-02-24 18:05:39.677833")
    
    class pv33:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/article_old.cfm/drama/43016"
           st_spider_date = str2datetime("2010-02-24 18:05:40.947105")
    
    class pv34:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/limelight.cfm"
           st_spider_date = str2datetime("2010-02-24 18:05:41.857705")
    
    class pv35:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.de/pages/reference.cfm/keltendorf"
           st_spider_date = str2datetime("2010-02-24 18:05:43.43859")
    
    class pv36:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/reference.cfm/disney_california_adventure"
           st_spider_date = str2datetime("2010-02-24 18:05:46.278631")
    
    class pv37:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "cruise-activities.suite101.com/topiclist/article.cfm/lively_alicante_for_activity_cruise_excursions"
           st_spider_date = str2datetime("2010-02-24 18:05:48.13671")
    
    class pv38:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "role-playing-video-games.suite101.com/topiclist/article.cfm/warrior_armor_guide_in_runescape"
           st_spider_date = str2datetime("2010-02-24 18:05:49.123701")
    
    class pv39:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "americanhistory.suite101.com/topiclist/article.cfm/benjamin-franklin-hires-a-pirate"
           st_spider_date = str2datetime("2010-02-24 18:05:52.868403")
    
    class pv40:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/exotic_wildlife/30676/1"
           st_spider_date = str2datetime("2010-02-24 18:05:53.353532")
    
    class pv41:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "www.suite101.com/pages/reference.cfm/designations"
           st_spider_date = str2datetime("2010-02-24 18:05:53.582654")
    
    class pv42:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/limelight.cfm"
           st_spider_date = str2datetime("2010-02-24 18:05:55.506214")
    
    class pv43:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/soapmaking/108940/2"
           st_spider_date = str2datetime("2010-02-24 18:05:56.151246")
    
    class pv44:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "www.suite101.com/pages/reference.cfm/atari_gifts"
           st_spider_date = str2datetime("2010-02-24 18:05:57.474588")
    
    class pv45:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "www.suite101.com/pages/reference.cfm/image_archive_software"
           st_spider_date = str2datetime("2010-02-24 18:05:59.548201")
    
    class pv46:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "www.suite101.com/pages/reference.cfm/gamma_hydroxybutyric_acid"
           st_spider_date = str2datetime("2010-02-24 18:06:01.673856")
    
    class pv47:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "www.suite101.com/301/discussion.cfm/oriental_history/34472/231530"
           st_spider_date = str2datetime("2010-02-24 18:06:03.145899")
    
    class pv48:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/reiki_world/99071/3"
           st_spider_date = str2datetime("2010-02-24 18:06:05.578513")
    
    class pv49:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "cryptozoology.suite101.com/topiclist/article.cfm/mothman_winged_anomaly_from_wv"
           st_spider_date = str2datetime("2010-02-24 18:06:06.409644")
    
    class pv50:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/1102/12539"
           st_spider_date = str2datetime("2010-02-24 18:06:06.822613")
    
    class pv51:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "www.suite101.com/pages/reference.cfm/guidelines_to_responsible_drinking"
           st_spider_date = str2datetime("2010-02-24 18:06:07.10136")
    
    class pv52:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "www.suite101.com/pages/article_old.cfm/elderly_caregiving/4099"
           st_spider_date = str2datetime("2010-02-24 18:06:08.70969")
    
    class pv53:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "www.suite101.com/pages/reference.cfm/divas"
           st_spider_date = str2datetime("2010-02-24 18:06:09.328497")
    
    class pv54:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/reference.cfm/sesame"
           st_spider_date = str2datetime("2010-02-24 18:06:09.527922")
    
    class pv55:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/animated_films/93645/1"
           st_spider_date = str2datetime("2010-02-24 18:06:09.695517")
    
    class pv56:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/article_old.cfm/relocation/61892/2"
           st_spider_date = str2datetime("2010-02-24 18:06:09.768928")
    
    class pv57:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/real_estate/44697/2"
           st_spider_date = str2datetime("2010-02-24 18:06:10.80256")
    
    class pv58:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/reference.cfm/type_ii_diabetes"
           st_spider_date = str2datetime("2010-02-24 18:06:13.198222")
    
    class pv59:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/reference.cfm/gords"
           st_spider_date = str2datetime("2010-02-24 18:06:15.732903")
    
    class pv60:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/reference.cfm/ways_to_build_credit_as_a_us_immigrant"
           st_spider_date = str2datetime("2010-02-24 18:06:15.920262")
    
    class pv61:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "preschool-tv.suite101.com/topiclist/article.cfm/four_first_ladies_visit_sesame_street"
           st_spider_date = str2datetime("2010-02-24 18:06:16.675102")
    
    class pv62:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "freeware-shareware.suite101.com/topiclist/article.cfm/backtoschool_applications_to_keep_files_safe"
           st_spider_date = str2datetime("2010-02-24 18:06:19.653796")
    
    class pv63:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/reference.cfm/2009_tall_ships_race_belfast"
           st_spider_date = str2datetime("2010-02-24 18:06:21.534617")
    
    class pv64:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "recipes.suite101.com/topiclist/article.cfm/lowcalorie_muffin_recipes_for_a_healthy_diet"
           st_spider_date = str2datetime("2010-02-24 18:06:22.738233")
    
    class pv65:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/reference.cfm/250_watt"
           st_spider_date = str2datetime("2010-02-24 18:06:23.009004")
    
    class pv66:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "bakingdesserts.suite101.com/topiclist/article.cfm/glutenfree_grains_and_flours"
           st_spider_date = str2datetime("2010-02-24 18:06:26.872644")
    
    class pv67:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "judaism.suite101.com/topiclist/default.cfm"
           st_spider_date = str2datetime("2010-02-24 18:06:27.624783")
    
    class pv68:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/article_old.cfm/mothers_and_daughters/70022"
           st_spider_date = str2datetime("2010-02-24 18:06:29.038891")
    
    class pv69:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "www.suite101.com/pages/limelight.cfm"
           st_spider_date = str2datetime("2010-02-24 18:06:30.424761")
    
    class pv70:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/sports_commentary/37046/1"
           st_spider_date = str2datetime("2010-02-24 18:06:34.065238")
    
    class pv71:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "www.suite101.com/pages/reference.cfm/scheduling_a_meeting_with_a_professor_or_ta"
           st_spider_date = str2datetime("2010-02-24 18:06:35.414765")
    
    class pv72:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/health_scams/18235/1"
           st_spider_date = str2datetime("2010-02-24 18:06:36.411371")
    
    class pv73:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/plastic_surgery/34573/1"
           st_spider_date = str2datetime("2010-02-24 18:06:37.312945")
    
    class pv74:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/biographies_scientists/101664/1"
           st_spider_date = str2datetime("2010-02-24 18:06:38.244863")
    
    class pv75:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/caring_soul/100867/2"
           st_spider_date = str2datetime("2010-02-24 18:06:39.745496")
    
    class pv76:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "flyfishing.suite101.com/topiclist/article.cfm/monster_bonefish_of_the_bahamas"
           st_spider_date = str2datetime("2010-02-24 18:06:39.860488")
    
    class pv77:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/historic_preservation/51824/1"
           st_spider_date = str2datetime("2010-02-24 18:06:40.175606")
    
    class pv78:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/301/discussions.cfm/wizard_of_oz/20-39"
           st_spider_date = str2datetime("2010-02-24 18:06:41.053105")
    
    class pv79:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "www.suite101.com/pages/reference.cfm/african_american_wedding"
           st_spider_date = str2datetime("2010-02-24 18:06:41.552723")
    
    class pv80:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/945/30963"
           st_spider_date = str2datetime("2010-02-24 18:06:42.625789")
    
    class pv81:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/united_methodist/53122/1"
           st_spider_date = str2datetime("2010-02-24 18:06:43.276454")
    
    class pv82:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/romance_retired/6357"
           st_spider_date = str2datetime("2010-02-24 18:06:44.714851")
    
    class pv83:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/reference.cfm/rhine_cruise"
           st_spider_date = str2datetime("2010-02-24 18:06:51.518289")
    
    class pv84:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/literary_theory_explorations/85532/1"
           st_spider_date = str2datetime("2010-02-24 18:06:51.931235")
    
    class pv85:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/indo_anglian_fiction/95988/1"
           st_spider_date = str2datetime("2010-02-24 18:06:52.559412")
    
    class pv86:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "entertaining.suite101.com/topiclist/article.cfm/more_team_party_ideas"
           st_spider_date = str2datetime("2010-02-24 18:06:52.672187")
    
    class pv87:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/reference.cfm/benefits_of_writers_conferences"
           st_spider_date = str2datetime("2010-02-24 18:06:54.339829")
    
    class pv88:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "ghosts-hauntings.suite101.com/topiclist/article.cfm/larrabee_st_haunting_hoax_real"
           st_spider_date = str2datetime("2010-02-24 18:06:57.740131")
    
    class pv89:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/breastcancer/64087/2"
           st_spider_date = str2datetime("2010-02-24 18:06:59.857665")
    
    class pv90:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/writer_articles.cfm/coachjerry"
           st_spider_date = str2datetime("2010-02-24 18:07:02.238668")
    
    class pv91:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/reference.cfm/charm_school_finale"
           st_spider_date = str2datetime("2010-02-24 18:07:03.128567")
    
    class pv92:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/video_scripting/20977/1"
           st_spider_date = str2datetime("2010-02-24 18:07:04.090071")
    
    class pv93:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/301/print_message.cfm/virtually_gardening/53685/400793"
           st_spider_date = str2datetime("2010-02-24 18:07:14.135065")
    
    class pv94:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/cult_cinema/106587/2"
           st_spider_date = str2datetime("2010-02-24 18:07:21.905332")
    
    class pv95:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "www.suite101.de/pages/sitemap.cfm/topic/leverkusen"
           st_spider_date = str2datetime("2010-02-24 18:07:27.735934")
    
    class pv96:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "www.suite101.com/pages/reference.cfm/overseas_property_insurance"
           st_spider_date = str2datetime("2010-02-24 18:07:27.830419")
    
    class pv97:
           st_user_agent = "mozilla/5.0 (compatible; yahoo! slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
           st_url = "www.suite101.com/pages/reference.cfm/leona_lewis_debut_album_spirit"
           st_spider_date = str2datetime("2010-02-24 18:07:29.389255")
    
    class pv98:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "www.suite101.com/pages/reference.cfm/colonic_atlanta"
           st_spider_date = str2datetime("2010-02-24 18:07:29.669823")
    
    class pv99:
           st_user_agent = "mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)"
           st_url = "www.suite101.com/pages/article_old.cfm/bathcrafts_candles/74052/1"
           st_spider_date = str2datetime("2010-02-24 18:07:32.76213")
    
    class pv100:
           st_user_agent = "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
           st_url = "www.suite101.com/pages/reference.cfm/cain_cuvee"
           st_spider_date = str2datetime("2010-02-24 18:07:32.92954")

