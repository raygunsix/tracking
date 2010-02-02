import logging
import datetime
import simplejson as json

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from tracking.lib.base import BaseController, render

from tracking.model import Pageviews
from tracking.model.meta import Session
from pylons.decorators import jsonify

from tracking import model

#from formencode.api import Invalid
#from pylons import url


log = logging.getLogger(__name__)

class PageviewsController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('pageview', 'pageviews')

    def index(self, format='html'):
        """GET /pageviews: All items in the collection"""
        # url('pageviews')
        pv_q = Session.query(Pageviews)
        c.pvs = pv_q.all()
        return render('/pageviews/index.mako')
        
    def create(self):
        """POST /pageviews: Create a new item"""
        # url('pageviews')
    
        jsn = json.loads(request.body)
        
        pv_q = Session.query(Pageviews)
        new_pv = Pageviews()
  
        new_pv.st_user_agent = jsn['st_user_agent']
        new_pv.st_url = jsn['st_url']
        new_pv.st_spider_date = datetime.datetime.now()
        
        Session.save(new_pv)
        Session.commit()
        
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
