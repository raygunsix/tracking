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


#deploy from github
#create tag 
#build egg from src
#copy new egg to server
#install / upgrade egg
#restart apache
#create tag 

# globals
env.project_name = 'tracking'
d = strftime("%Y-%m-%d-%H%M%S", gmtime())

# environments
def qa():
    #env.fab_user = 'ubuntu'
    env.hosts = ['ubuntu@tracking.dev.suite101.com']
    env.releases_path = '/home/ubuntu/releases/'

# tasks
def build():
    local("python setup.py bdist_egg")

def cleanup():
    local("rm -rf build/*")
    #local("rm -rf dist/*.egg")


def restart_webserver():
    "Restart the web server"
    sudo('/etc/init.d/apache2 restart')


# deployment
def deploy():
   "Deploy code to servers"
   build()
   put("dist/*.egg", env.releases_path + env.project_name + "-" + d + ".egg")
   cleanup()

