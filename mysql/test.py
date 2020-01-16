import pymysql

conn = pymysql.connect(host="127.0.0.1", port = 3307,user="root",password="123456",database="school",charset="utf8")

cursor = conn.cursor()
'''
cursor.execute("select * from student")
res = cursor.fetchall()
for row in res:
    print(row)
    for str in row:
        print(str)
'''
colunm = ["姓名", "得分", "投篮", "命中", "出手", "时间", "篮板", "助攻", "抢断", "盖帽",
         "失误", "罚球命中", "罚球总数","三分命中", "三分出手","输赢","对手分区"]
sql = "INSERT into PLAYER_DATA(姓名, 得分, 投篮, 命中, 出手, 时间, 篮板, 助攻, 抢断, 盖帽,失误, 罚球命中, " \
      "罚球总数,三分命中, 三分出手,输赢,对手分区) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

cursor.execute(sql,['勒布朗-詹姆斯', '25', '60.0%', '12', '20', '42', '6', '9', '4', '0', '2', '1', '3', '0', '2', 'lose', '西部'])
#cursor.executemany(sql,[[81,"aisa"],[84,"aisa"]])
conn.commit()


conn.close()

