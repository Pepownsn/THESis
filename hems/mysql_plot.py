import MySQLdb
import time
import datetime
import re
import urllib2
import socket
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np

conn= MySQLdb.connect("52.220.88.45","read","hems","power") # One Pi 1 @192.168.1.25 namal localhost
c = conn.cursor()

c.execute("SELECT s11  FROM power.enegate_bkk WHERE Timestamp >= '2016-08-10 00:00:00' AND Timestamp < '2016-08-10 01:00:00' ")
results = c.fetchall()

power = []
time = []
i = 0
for row in results:
   # if row[0] == "----":
       # print row[0]
   # else :power.append(row[0])
print len(power)

for i in range(len(power)):
    time.append(i+1)

#print time
#print power


##time.plot()
#power.plot()
plt.scatter(time,power)
#plt.legend(loc=4)
##plt.show()
plt.savefig('plots.png', dpi=1000)

conn.commit()
