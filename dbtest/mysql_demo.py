import pymysql

db = pymysql.Connect(host='127.0.0.1', port=3306, user='root', db='test', password='')

cursor = db.cursor()

sql = "select * from account"

try:
    cursor.execute(sql)
    res = cursor.fetchall()
    print(res)
    for row in res:
        print("name:%s, age:%d" % (row[0], row[1]))
except:
    print("error, can't query record from db")

db.close()
