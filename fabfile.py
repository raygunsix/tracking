from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
from datetime import datetime, date, time
from time import gmtime, strftime

##########
# To do
##########
#
# Add milliseconds to datetime stamp
# strftime("%Y%m%d-%H%M%S%f") doesn't seem to work... not sure why
# Or maybe use the git rev string instead?
# i.e. r = git show --abbrev-commit | grep "^commit";
#
# deploy from github?
# create tag after deploy?
#
# show installed egg version()
# i.e. /usr/local/pylons/tracking/env/bin/pip freeze | grep tracking
#
# setup() function to create releases dir strcture?
# check() to verify env - paths, apache etc.
#
# Make sure we're putting correct egg file - don't use wildcard

# globals
env.project_name = 'tracking'
d = strftime("%Y.%m.%d.%H%M%S", gmtime())

# environments
def qa():
    env.hosts = ['ubuntu@tracking.qa.suite101.com']
    env.releases_path = '/home/ubuntu/releases/' + env.project_name + "/"
    env.python_env_path = '/usr/local/pylons/' + env.project_name + '/env/'
    
# tasks
def test():
    local("nosetests")

def build():
    local("python setup.py bdist_egg")

def upload():
    put("dist/*.egg", env.releases_path + env.project_name + "-" + d + ".egg")

def install():
    sudo(env.python_env_path + "bin/easy_install -U " + env.releases_path + env.project_name + "-" + d + ".egg")

def restart_webserver():
    "Restart the web server"
    sudo('/etc/init.d/apache2 restart')

def cleanup():
    local("rm -rf build/*")
    local("rm -rf dist/*.egg")
    local("rm -rf *.egg")    

# deployment
def deploy():
   "Deploy code to servers"
   test()
   build()
   upload()
   install()
   restart_webserver()
   cleanup()

