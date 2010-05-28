import site
import os, sys

site.addsitedir('/usr/local/pylons/tracking/env/lib/python2.6/site-packages')

sys.path.append('/usr/local/pylons/tracking/')
os.environ['PYTHON_EGG_CACHE'] = '/tmp/python-eggs'

from paste.script.util.logging_config import fileConfig

fileConfig('/usr/local/pylons/tracking/development.ini')

from paste.deploy import loadapp

application = loadapp('config:/usr/local/pylons/tracking/production.ini')
