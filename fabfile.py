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
#deploy from github?
#create tag after deploy?
#install / upgrade egg

# globals
env.project_name = 'tracking'
d = strftime("%Y-%m-%d-%H%M%S", gmtime())

# environments
def qa():
    #env.fab_user = 'ubuntu'
    env.hosts = ['ubuntu@tracking.dev.suite101.com']
    env.releases_path = '/home/ubuntu/releases/'
    env.project_path = '/usr/local/pylons/'
    
# tasks
def build():
    local("python setup.py bdist_egg")

def install():
    sudo(env.project_path + env.project_name + "/env/bin/easy_install -U " + env.releases_path +  env.project_name + "-" + d + ".egg")

def restart_webserver():
    "Restart the web server"
    sudo('/etc/init.d/apache2 restart')

def cleanup():
    local("rm -rf build/*")
    local("rm -rf dist/*.egg")

# deployment
def deploy():
   "Deploy code to servers"
   build()
   put("dist/*.egg", env.releases_path + env.project_name + "-" + d + ".egg")
   install()
   restart_webserver()
   cleanup()

