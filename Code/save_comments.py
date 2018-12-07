import pymysql

db = pymysql.connect(host='localhost', user='root', password='diandichunjing', port=3306, db='mifei')

f = open('content.txt', 'w', encoding='utf-8')

cursor = db.cursor()
sql = 'select content from comments'
cursor.execute(sql)
results = cursor.fetchall()
print('读取成功！')

for row in results:
	f.write(row[0] + '\n')

db.close()

print('保存成功！')