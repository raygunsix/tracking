import logging
import datetime
import pymongo
import simplejson as json

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from paste.deploy import appconfig
from pylons import config
from tracking.config.environment import load_environment

from tracking.lib.base import BaseController, render

from tracking.model import Pageviews
from tracking.model.meta import Session
from pylons.decorators import jsonify

from tracking import model

from pymongo import Connection

#from formencode.api import Invalid
#from pylons import url


log = logging.getLogger(__name__)

mongodb_host = config['mongodb_host']
mongodb_port = int(config['mongodb_port'])

class PageviewsController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('pageview', 'pageviews')

    def index(self, format='html'):
        """GET /pageviews: All items in the collection"""
        # url('pageviews')
        pass
        
    def create(self):
        """POST /pageviews: Create a new item"""
        """This intrerface is deprecated - data should be sent via AWS SQS"""
        # url('pageviews')
    
	try:
	    jsn = json.loads(request.body)
        except:
            abort(status_code=500, detail="Could not parse JSON")
        
        # Write to postgreSQL via SQLAlchemy
        
        new_pv = Pageviews()
  
        new_pv.user_agent = jsn['st_user_agent']
        new_pv.url = jsn['st_url']
        new_pv.spider_date = datetime.datetime.now()
        
        Session.add(new_pv)
        
	try:
	    Session.commit()
        except:
            abort(status_code=500, detail="Could not save data to PostgreSQL")
        
        # Write to mongodb
        
        connection = Connection()
        connection = Connection(mongodb_host, mongodb_port)

        db = connection.tracking
        
        new_pv = {"user_agent": jsn['st_user_agent'],
            "url": jsn['st_url'],
             "date": datetime.datetime.utcnow()}
        
        pv = db.pageviews
        
        try:
	    pv.insert(new_pv)
        except:
            abort(status_code=500, detail="Could not save data to MongoDB")
        
    def new(self, format='html'):
        """GET /pageviews/new: Form to create a new item"""
        # url('new_pageview')
        pass

    def update(self, id):
        """PUT /pageviews/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('pageview', id=ID),
        #           method='put')
        # url('pageview', id=ID)
        pass

    def delete(self, id):
        """DELETE /pageviews/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('pageview', id=ID),
        #           method='delete')
        # url('pageview', id=ID)
        pass

    def show(self, id, format='html'):
        """GET /pageviews/id: Show a specific item"""
        # url('pageview', id=ID)
        pass

    def edit(self, id, format='html'):
        """GET /pageviews/id/edit: Form to edit an existing item"""
        # url('edit_pageview', id=ID)
        pass
