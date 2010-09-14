#!/usr/local/pylons/tracking/env/bin/python

"""
Script that fetches data from an AWS SQS queue and saves it in the database
"""
 
import boto
import simplejson as json
import datetime
import psycopg2
import psycopg2.extras

from boto.sqs.message import Message

# Set up constants
 
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
QUEUE_NAME = ""
DB_HOST = ""
DB_NAME = ""
DB_USER = ""
DB_PASSWORD = ""

# Set up connections to AWS services
 
conn = boto.connect_sqs(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
q = conn.get_queue(QUEUE_NAME)

# set up db

conn_str = "host='" + DB_HOST + "' dbname='" + DB_NAME + "' user='" + DB_USER + "' password='" + DB_PASSWORD + "'"

connection=psycopg2.connect(conn_str)

cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Functions
    
def get_msg():
    """Reads JSON formatted messages from the queue, saves to the database
        and deletes the messages
    """
    
    msgs = q.get_messages(10, visibility_timeout=120)
    
    for msg in msgs:
        
        jsn = json.loads(msg.get_body())
        
        user_agent = jsn['user_agent']
        url = jsn['url']
        spider_date = datetime.datetime.now()

	sql = "INSERT INTO pageviews(user_agent, url, spider_date) VALUES ('" + user_agent + "', '" + url + "', '" + str(spider_date) + "')"
        cursor.execute(sql)
        connection.commit()
        
        q.delete_message(msg)

    
get_msg()







