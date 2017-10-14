import MySQLdb
import time
import datetime
import re
import urllib2
import socket

while (True):

    try:
        s = socket.socket()
        s.connect(('skyfighter.ddns.net',10070))
        en_conn = True
        print "Socket_Connect OK"
    except socket.error, exc:
        print "Caught exception socket.error : %s" % exc
        print "Can't Connect "
        en_conn = False

"""
try:
    enegate_conn = urllib2.urlopen("http://skyfighter.ddns.net:10070/index.cgi")
    response = enegate_conn.read()
    print "Urllib_Connecting"
    en_conn = True
except urllib2.HTTPError as err:
    if err.code == 404:
        print "Can't Connect ERROR 404 "
        en_conn = False
    else:
        raise
        print "Can't Connect other "
        en_conn = False
"""
