#
#  csv2fixture-pv.py
#
#  Script converts csv file dump of pageviews table to fixture class format
#
#  Usage:
#
#  1) Dump the pageviews table from production to a csv file
#
#  2) Create an empty output file (ie touch pvclasses.txt)
#
#  3) Put input, output and script files in the same directory
#
#  4) Run the script (ie python csv2fixture-pv.py)
#
#  5) Edit the output file to clean up the data
#
#  6) Paste data into datasets/pageviews.py
#
#  7) Run paster setup-app development.ini to re-populate database
#
#
#  Notes:
#
#  The script doesn't handle null values really well... you may have to delete
#  the entry from the class before running setup
#

import csv
from datetime import datetime
from cStringIO import StringIO

infile = '/Users/chris/Desktop/pageviews.csv'
outfile = '/Users/chris/Desktop/pvclasses.txt'

s = StringIO()
reader = csv.DictReader(open(infile))
writer = open(outfile, 'r+')
id = 0

for row in reader:
    id += 1
    writer.write('class pv' + str(id) + ':' + '\n')
    writer.write('       st_user_agent = "' + row['st_user_agent'] + '"' + '\n')
    writer.write('       st_url = "' + row['st_url'] + '"' + '\n')
    writer.write('       st_spider_date = str2datetime("' + row['st_spider_date'] + '")' + '\n')
    writer.write('\n')

writer.close
