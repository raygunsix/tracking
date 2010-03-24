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
 
AWS_ACCESS_KEY_ID = "AKIAJYFRU4OEDOHDRBHQ"
AWS_SECRET_ACCESS_KEY = "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"
QUEUE_NAME = "tracking"
DB_HOST = "localhost"
DB_NAME = "tracking"
DB_USER = "webserver"
DB_PASSWORD = "suite101"

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
        
        st_user_agent = jsn['st_user_agent']
        st_url = jsn['st_url']
        st_spider_date = datetime.datetime.now()

	sql = "INSERT INTO pageviews(st_user_agent, st_url, st_spider_date) VALUES ('" + st_user_agent + "', '" + st_url + "', '" + str(st_spider_date) + "')"
        cursor.execute(sql)
        connection.commit()
        
        q.delete_message(msg)

    
get_msg()







