from tracking.tests import *
from routes import url_for
import simplejson as json
 
from sqlalchemy import and_

from tracking.model import Pageviews
from tracking.model import meta
from tracking.model.meta import Session

class TestPageviewsController(TestController):

    def test_index(self):
        response = self.app.get(url('pageviews'))
        # Test response...

    def test_index_as_xml(self):
        response = self.app.get(url('formatted_pageviews', format='xml'))

    def test_create(self):
        """Tests that json data can be posted and saved to the database"""
        
        response = self.app.post(
            url=url_for(controller='pageviews', action='create'),
            params=json.dumps({
                'st_user_agent':'mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)',
                'st_url':'cookingresources.suite101.com/topiclist/article.cfm/ban_the_gut_bomb',
            }),
            extra_environ=dict(CONTENT_TYPE='application/json')
        )
        self.failUnlessEqual(response.status, '200 OK')
        
        # Test the data is saved in the database (we use the engine API to
        # ensure that all the data really has been saved and isn't being returned
        # from the session)
        connection = meta.engine.connect()
        result = connection.execute(
            """
            SELECT st_user_agent, st_url
            FROM pageviews
            """,
        )
        connection.close()
        row = result.fetchone()
        assert row.st_user_agent == 'mozilla/5.0 (compatible; googlebot/2.1; +http://www.google.com/bot.html)'
        assert row.st_url == 'cookingresources.suite101.com/topiclist/article.cfm/ban_the_gut_bomb'        
        

    def test_new(self):
        response = self.app.get(url('new_pageview'))

    def test_new_as_xml(self):
        response = self.app.get(url('formatted_new_pageview', format='xml'))

    def test_update(self):
        response = self.app.put(url('pageview', id=1))

    def test_update_browser_fakeout(self):
        response = self.app.post(url('pageview', id=1), params=dict(_method='put'))

    def test_delete(self):
        response = self.app.delete(url('pageview', id=1))

    def test_delete_browser_fakeout(self):
        response = self.app.post(url('pageview', id=1), params=dict(_method='delete'))

    def test_show(self):
        response = self.app.get(url('pageview', id=1))

    def test_show_as_xml(self):
        response = self.app.get(url('formatted_pageview', id=1, format='xml'))

    def test_edit(self):
        response = self.app.get(url('edit_pageview', id=1))

    def test_edit_as_xml(self):
        response = self.app.get(url('formatted_edit_pageview', id=1, format='xml'))
