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

from formencode.api import Invalid
from pylons import url


log = logging.getLogger(__name__)

class PageviewsController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('pageview', 'pageviews')

    #def __before__(self):
    #    self.pv_q = Session.query(Pageviews)

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
        #return s['content_id'] + " " + s['object_id'] + " " + s['referrer'] + " " + s['search_terms'] + " " + s['user_agent']
        
        pv_q = Session.query(Pageviews)
        new_pv = Pageviews()
  
        new_pv.content_id = jsn['content_id']
        new_pv.object_id = jsn['object_id']
        new_pv.search_terms = jsn['search_terms']
        new_pv.referrer = jsn['referrer']
        new_pv.user_agent = jsn['user_agent']
        new_pv.create_date = datetime.datetime.now()
        
        Session.save(new_pv)
        Session.commit()
        
        # need to send json response - @jsonify
        #return s['content_id'] + " " + s['object_id'] + " " + s['referrer'] + " " + s['search_terms'] + " " + s['user_agent']
        
    def new(self, format='html'):
        """GET /pageviews/new: Form to create a new item"""
        # url('new_pageview')
        
        test = request.GET
        s = json.dumps({"content_id": request.params['content_id'], "object_id": request.params['object_id'], "referrer": request.params['referrer'], "search_terms": request.params['search_terms'], "user_agent": request.params['user_agent']}, sort_keys=True)
        return s
        
        #pv_q = Session.query(Pageviews)
        #new_pv = Pageviews()
        
        #c.content_id = request.params['content_id']
        #c.object_id = request.params['object_id']
        #c.search_terms = request.params['search_terms']
        #c.referrer = request.params['referrer']
        #c.user_agent = request.params['user_agent']

        #new_pv.content_id = request.params['content_id']
        #new_pv.object_id = request.params['object_id']
        #new_pv.search_terms = request.params['search_terms']
        #new_pv.referrer = request.params['referrer']
        #new_pv.user_agent = request.params['user_agent']
        #new_pv.create_date = datetime.datetime.now()
        
        #Session.save(new_pv)
        #Session.commit()
        
        
        #return render('/pageviews/new.mako') 

    def update(self, id):
        """PUT /pageviews/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('pageview', id=ID),
        #           method='put')
        # url('pageview', id=ID)

    def delete(self, id):
        """DELETE /pageviews/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('pageview', id=ID),
        #           method='delete')
        # url('pageview', id=ID)

    def show(self, id, format='html'):
        """GET /pageviews/id: Show a specific item"""
        # url('pageview', id=ID)

    def edit(self, id, format='html'):
        """GET /pageviews/id/edit: Form to edit an existing item"""
        # url('edit_pageview', id=ID)
