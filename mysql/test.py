import pymysql

conn = pymysql.connect(host="127.0.0.1", port = 3307,user="root",password="123456",database="school",charset="utf8",autocommit = "true")

cursor = conn.cursor()
'''
cursor.execute("select * from student")
res = cursor.fetchall()
for row in res:
    print(row)
    for str in row:
        print(str)
'''
sql = "INSERT into student(id,name) values (85,\"python\");"
cursor.execute(sql)

conn.close()

