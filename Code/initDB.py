import pymysql

# PIG 连接Mysql数据库
db = pymysql.connect(host='localhost', user='root', password='diandichunjing', port='3306', db='mifei') 

#PIG 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

#PIG 使用execute()方法执行SQL语句
#cursor.execute('SELECT VERSION()')

#PIG 使用fetchone()方法获取单条数据
#data = cursor.fetchone()

#print('Database version:', data)

#PIG 创建新的数据库
#cursor.execute('CREATE DATABASE mifei')

sql = '''
		 create table comments(
		 id 			char(11) primary key,
		 creationTime 	datetime(),
		 content		varchar(200),
		 productColor	varchar(10),
		 userClientShow varchar(20)
		 )
	  '''
cursor.execute(sql)

db.close()
