#!/usr/bin/env python

import os, sys
sys.path.append('/var/www/tracking.dev.suite101.com/htdocs')
os.environ['PYTHON_EGG_CACHE'] = '/tmp/python-eggs'

from paste.deploy import loadapp

application = loadapp('config:/var/www/tracking.dev.suite101.com/htdocs/testing.ini')

