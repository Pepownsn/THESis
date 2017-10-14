import matplotlib.pyplot as plt
import pandas
import MySQLdb

# connect to MySQL database
conn = MySQLdb.connect("52.220.88.45","read","hems","power")


query = """
SELECT TimeStamp, s11
FROM power.enegate_bkk
WHERE TimeStamp >= "2016-08-07 00:00:00"
  AND TimeStamp < "2016-08-14 00:00:00";
"""

df = pandas.read_sql(query, conn, index_col=['TimeStamp'])

df = df[df.s11 != "----"]


#df['s14'] = df['s14'].astype(int)
df['s11'] = df['s11'].astype(int)
#df['SUM'] = df['s11'] + df['s13']



fig, ax = plt.subplots()
ax.set_title('07-14 Aug 2016')
df.plot(ax=ax)
plt.show()
conn.close()
