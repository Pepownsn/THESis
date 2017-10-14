import MySQLdb
import time
import datetime
import pandas as pd
import urllib2

conn= MySQLdb.connect("54.179.158.47","conn","hems","power")
c = conn.cursor()

query = """
SELECT TimeStamp, s11
FROM power.enegate_bkk
WHERE TimeStamp >= "2016-09-01 00:00:00"
  AND TimeStamp < "2016-09-02 0:00:00";
"""

df = pd.read_sql(query, conn)
df = df[df.s11 != "----"]
df = df.reset_index(df['s11'])
print df

# df['s11'] = df['s11'].astype(int)
# print df
#
# min_p = 0
# for i in range (len(df['s11'])):
#     min_p += df.'s11[i]''
# min_p = min_p/
