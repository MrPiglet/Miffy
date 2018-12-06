import requests
import csv
import json
import time

def getCom(url, pn): #PIG 输入网址和页码，获取评论
	myHeaders = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
	}
	r = requests.get(url,headers = myHeaders)
	r.encoding = r.apparent_encoding
	r = r.text
	r = r.replace('fetchJSON_comment98vv10734(','')
	r = r.replace(');','')
	page = json.loads(r)
	return page

def parseCom(com):
    comList = []
    res = com['comments']
    for i in res:
        comInfo = []
        comInfo.append(i['creationTime'])
        comInfo.append(i['content'])
        comInfo.append(i['referenceName'])
        comList.append(comInfo)
    return comList

def main():
    pn = 10
    comList = []
    csvfile = open('mifei.csv', 'a', newline='', encoding='utf-8-sig')
    for i in range(1, pn+1):
	    url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv10734&productId=12879814840&score=0&sortType=5&page='+str(i)+'&pageSize=10&isShadowSku=0&fold=1'
	    com = getCom(url, pn)
	    comList = parseCom(com)
	    writer = csv.writer(csvfile)
	    for c in comList:
	    	writer.writerow(c)
	    print('第%d页处理成功'%i)
	    time.sleep(1)

if __name__ == '__main__':
	main()
