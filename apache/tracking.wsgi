#!/usr/local/pylons/tracking/env/bin/python

import site
site.addsitedir('/usr/local/pylons/tracking/env/lib/python2.6/site-packages')

import os, sys
sys.path.append('/usr/local/pylons/tracking/')
os.environ['PYTHON_EGG_CACHE'] = '/tmp/python-eggs'

from paste.deploy import loadapp

application = loadapp('config:/usr/local/pylons/tracking/production.ini')

