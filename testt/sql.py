import MySQLdb
import time
import datetime
import re
import urllib2
import socket

conn= MySQLdb.connect("52.220.88.45","read","hems","power") # One Pi 1 @192.168.1.25 namal localhost
c = conn.cursor()

c.execute("SELECT s11  FROM power.enegate_bkk WHERE Timestamp >= '2016-08-14 ' AND Timestamp < '2016-08-15' LIMIT 10")
results = c.fetchall()


power = []


for row in results:

    power.append(row[0])

print len(power)

print power


conn.commit()
