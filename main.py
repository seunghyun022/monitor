from sqlite3 import IntegrityError
import psutil
import pymysql
import mysql_auth
import socket
import datetime
import pytz
login = mysql_auth.Info

ip=socket.gethostbyname(socket.gethostname())
cpu=int(psutil.virtual_memory().percent)
mem=int(psutil.cpu_percent())
now=datetime.datetime.now(pytz.timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S')

conn = pymysql.connect(host=login['host'],user=login['user'],passwd=login['passwd'],db=login['db'],charset=login['charset'])
c= conn.cursor()
try:
    c.execute('INSERT INTO mon(Ip,Cpu,Mem,Updated) VALUES(%s,%s,%s,%s) ON DUPLICATE KEY UPDATE Cpu=%s, Mem=%s, Updated=%s',
    (ip,cpu,mem,now,cpu,mem,now))
    conn.commit()
except:
    print('insert failed')
conn.close

