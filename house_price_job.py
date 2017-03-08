# -*- encoding: utf8 -*-

import requests
import lxml
from lxml import etree
import time
from file_util import FileUtil

_house_url_list = [
'http://esf.hz.fang.com/chushou/3_197616209.htm',
'http://esf.hz.fang.com/chushou/3_198156508.htm',
'http://esf.hz.fang.com/chushou/3_197686566.htm',
'http://esf.hz.fang.com/chushou/3_197902953.htm',
'http://esf.hz.fang.com/chushou/3_198088904.htm',
'http://esf.hz.fang.com/chushou/3_195849081.htm',
'http://esf.hz.fang.com/chushou/3_197487187.htm',
'http://esf.hz.fang.com/chushou/3_198013879.htm',
'http://esf.hz.fang.com/chushou/3_198013763.htm',
'http://esf.hz.fang.com/chushou/3_198638614.htm',
'http://esf.hz.fang.com/chushou/3_198143564.htm',
'http://esf.hz.fang.com/chushou/3_197655717.htm',
'http://esf.hz.fang.com/chushou/3_194965518.htm',
'http://esf.hz.fang.com/chushou/3_198621886.htm',
'http://esf.hz.fang.com/chushou/3_197466546.htm',
'http://esf.hz.fang.com/chushou/3_194964600.htm',
'http://esf.hz.fang.com/chushou/3_194481373.htm',
'http://esf.hz.fang.com/chushou/3_197759484.htm',
'http://esf.hz.fang.com/chushou/3_198390667.htm',
'http://esf.hz.fang.com/chushou/3_198013882.htm',
'http://esf.hz.fang.com/chushou/3_194964600.htm',
'http://esf.hz.fang.com/chushou/3_197403605.htm',
'http://esf.hz.fang.com/chushou/3_198532619.htm',
'http://esf.hz.fang.com/chushou/3_197488515.htm'
]



class HousePrice():


	def get_all_house_url(self):
		file_handler = FileUtil()
		all_house_url = file_handler.read('/house_url.txt')
		house_url_list = all_house_url.split('\n')
		house_url_list = list(set(house_url_list))

		return house_url_list

	#数据取出来  去重
	def get_all_house_info_and_unique(self):
		file_handler = FileUtil()
		all_house_info = file_handler.read('/house_price.txt')
		house_info_list =  all_house_info.split('\n')
		house_info_list = list(set(house_info_list))

		str_house_info_list = '\n' +  '\n'.join(house_info_list)

		print file_handler.over_write('/house_price.txt', str_house_info_list)


	#单条房屋价格入库,不判断重，重复数据拉出来再处理
	def store_house_data(self,house_price_info):
		file_handler = FileUtil()
		result = file_handler.append_write('/house_price.txt', '\n' + str(house_price_info) + '\n')
		print result

	#获取html文本
	def getHtml(self,url):
		resp = requests.get(url)
		status_code = resp.status_code 
		if status_code == 200:
			return resp.text.encode('utf-8')
		else:
			print '页面加载不到'
			return None

	#提取房屋标题和总价
	def parse_house_info(slef,html):

		try:
			house_etree = etree.HTML(html)
			pass
		except Exception, e:
			print 'html 转 etree异常'
			return None
			
		

		house_title_x = house_etree.xpath('//div[@class="title"]/h1')

		house_price_x = house_etree.xpath('//div[@class="inforTxt"]/dl/dt/span[@class="red20b"]')

		house_title = '默认标题'
		if len(house_title_x) > 0:
			house_title = house_title_x[0].text.encode('utf-8').strip()

		house_price = "默认价格"
		if len(house_price_x) > 0:
			house_price = house_price_x[0].text.encode('utf-8')


		return str(house_price) + ',' + str(house_title)


	#获取信息并存储
	def get_hource_price_and_store(self):

		house_url_list = self.get_all_house_url()

		house_info_list = []
		for house_url in house_url_list:
			if house_url is not None:
				house_html = self.getHtml(house_url)
				house_info = ''
				if house_html is not None:
					house_info = self.parse_house_info(house_html)
					if house_info is None:
						print '异常链接' + str(house_url)
						continue	
					else:
						today_date_str = time.strftime('%Y%m%d')
						self.store_house_data(house_url + ',' + house_info + ',' + today_date_str)
		self.get_all_house_info_and_unique()





		






