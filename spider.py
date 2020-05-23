#-- coding:UTF-8 --
from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3
def main():
	baseurl="https://movie.douban.com/top250?start="
	datalist = getData(baseurl)
	savepath = ".\\豆瓣电影Top250.xls"
	#保存数据
	#saveData(savepath)
	askURL("https://movie.douban.com/top250?start=0")



#爬取网页
def getData(baseurl):
	datalist = []
        for i in range(0,10):               #调用获取页面信息的函数10次
            url = baseurl + str(i*25)
            html = askURL(url)              #保存已经获取到的网页源码
	    #2，逐一解析数据



	return datalist



#得到指定一个url的网页内容
def askURL(url):
				#模拟浏览器头部信息，向豆瓣服务器发送消息
	head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"}
				#用户代理，表示告诉豆瓣服务器，我们是什么样的浏览器，本质上是告诉服务器我们可以接受什么水平的文件内容
	request = urllib.request.Request(url,headers=head)
	html=""
	try:
		response = urllib.request.urlopen(request)
		html = response.read().decode("utf-8")
		print(html)
	except urllib.error.URLError as e:
		if hasattr(e,"code"):
			print(e.code)
		if hasattr(e,"reason"):
			print(e.reason)
	return html

#3，保存数据
def saveData(savepath):
	print("save....")




if __name__ == "__main__":
#调用函数
	main()
 
