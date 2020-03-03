from DBUtils.PersistentDB import PersistentDB
from DBUtils.PooledDB import PooledDB
import pymysql
import threading
import time

POOL = PooledDB(pymysql,5,host='127.0.0.1',user='root',passwd='123456',db='school',
                port=3307,charset="utf8") #5为连接池里的最少连接数


def select():
    conn = POOL.connection()  # conn = SteadyDBConnection()
    cursor = conn.cursor()
    cursor.execute('select * from PLAYER_DATA')
    result = cursor.fetchall()
    cursor.close()
    conn.close()  # 不是真的关闭，而是假的关闭。 conn = pymysql.connect()   conn.close()
    print(result)

def update(list):
    conn = POOL.connection()  # conn = SteadyDBConnection()
    cursor = conn.cursor()
    sql = "INSERT into PLAYER_DATA(姓名, 得分, 投篮, 命中, 出手, 时间, 篮板, 助攻, 抢断, 盖帽,失误, 罚球命中, " \
          "罚球总数,三分命中, 三分出手,输赢,对手分区) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    cursor.execute(sql,list)
    conn.commit()
    conn.close()  # 不是真的关闭，而是假的关闭。 conn = pymysql.connect()   conn.close()

list = ['勒布朗-詹姆斯', '28', '55.6%', '10', '18', '40', '7', '8', '2', '1', '4', '6', '8', '2', '4', 'lose', '东部']

#update(list)

'''
for i in range(10):
    t = threading.Thread(target=update,args=(list,))
    t.start()
    time.sleep(1)
'''