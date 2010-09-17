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
env.pylons_path = '/usr/local/pylons/'
d = strftime("%Y.%m.%d.%H%M%S", gmtime())

# environments
def qa():
    env.hosts = ['root@tracking.qa.suite101.com']
    env.releases_path = '/root/releases/' + env.project_name + "/"
    env.python_env_path = env.pylons_path + env.project_name + '/env/'

def live():
    env.hosts = ['ubuntu@tracking.suite101.com']
    env.releases_path = '/home/ubuntu/releases/' + env.project_name + "/"
    env.python_env_path = env.pylons_path + env.project_name + '/env/'
    
# tasks

def setup():

    print ("Creating directories")
    run("mkdir -p " + env.pylons_path + env.project_name + "/apache/")  
    run("mkdir " + env.pylons_path + env.project_name + "/data/")
    run("mkdir " + env.pylons_path + env.project_name + "/downloads/")
    run("mkdir " + env.pylons_path + env.project_name + "/lib/")
    run("mkdir " + env.pylons_path + env.project_name + "/scripts/")
    run("mkdir " + env.pylons_path + env.project_name + "/sqs/")
    run("mkdir -p /root/releases/" + env.project_name + "/")
    run("mkdir -p /var/log/" + env.project_name + "/")
    
    # Set permissions
    run("chmod -R a+rwx " + env.pylons_path + env.project_name + "/data/")
    
    # Create virtual env
    run("virtualenv --no-site-packages " + env.pylons_path + env.project_name + "/env/")
    
    # Install Python PostgreSQL driver into virtual environment
    run(env.python_env_path + "bin/easy_install psycopg2")
    
    # Print post-setup tasks
    print (" ")
    print ("== POST SETUP TASKS ==")
    print ("* Deploy the app")
    print ("* Add pylons config file")
    print ("* Setup database and users")
    print ("* Install the pylons app - 'python setup.py develop'")
    print ("* Run app set up - 'paster setup-app'")
    
def test():
    local("nosetests")

def build():
    local("python setup.py bdist_egg")

def upload():
    put("dist/*.egg", env.releases_path + env.project_name + "-" + d + ".egg")

def install():
    run(env.python_env_path + "bin/easy_install -U " + env.releases_path + env.project_name + "-" + d + ".egg")

def restart_webserver():
    "Restart the web server"
    run('service apache2 restart')

def cleanup():
    local("rm -rf build/*")
    local("rm -rf dist/*.egg")
    local("rm -rf *.egg")    

# deployment
def deploy():
   "Deploy code to servers"
   #test()
   build()
   upload()
   install()
   restart_webserver()
   cleanup()

