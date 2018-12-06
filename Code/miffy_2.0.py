import requests
import csv
import json
import time
import pymysql

def getCom(url, pn): #PIG 输入网址和页码，获取评论
	try:
		myHeaders = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
		'referer': 'https://item.jd.com/12879814840.html'
		}
		r = requests.get(url,headers = myHeaders)
		r.encoding = r.apparent_encoding
		r.raise_for_status()
		r = r.text
		#r = r.replace('fetchJSON_comment98vv10734(','')
		#r = r.replace(');','')
		page = json.loads(r)
		return page
	except:
		print('第%d页出错' % pn)
	

def parseCom(com):
    comList = []
    res = com['comments']
    for i in res:
        comInfo = []
        comInfo.append(i['id'])
        comInfo.append(i['creationTime'])
        comInfo.append(i['content'])
        comInfo.append(i['productColor'])
        comInfo.append(i['userClientShow'])
        comList.append(comInfo)
    return comList

def saveComToDB():
	db = pymysql.connect(host='localhost', user='root', password='diandichunjing', port=3306 db='mifei')
	cursor = db.cursor()
	sql = 'insert into comments values (%s, %s, %s, %s, %s)'
	pn = 49
	for i in range(1, pn):
		try:
			url = 'https://sclub.jd.com/comment/productPageComments.action?productId=12879814840&score=0&sortType=5&page='+str(i)+'&pageSize=10&isShadowSku=0&rid=0&fold=1'
			res = getCom(url, i)
			com = parseCom(res)
			for val in com:
				try:
					cursor.execute(sql, (val[0], val[1], val[2], val[3], val[4]))
					db.commit()
				except:
					db.rollback()
			print('第%d页成功' % i)
			time.sleep(1)
		except:
			print('第%d页出错' % i)
			time.sleep(1)
	db.close()
	print('保存成功')

if __name__ == '__main__':
	saveComToDB()
