from scrapy.selector import Selector
from scrapy.spider import Spider
from scrapy.http import Request
from news.items import ArticleItem
import json
import os.path

class ArticleSpider(Spider):
	name = 'bbcarticle'
	allowed_domains = ['http://www.bbc.co.uk/news/', 'http://www.bbc.co.uk', 'http://www.bbc.com']
	parentDir = os.path.abspath(os.path.join(__file__, os.pardir))
	parentDir = os.path.abspath(os.path.join(parentDir, os.pardir))
	parentDir = os.path.abspath(os.path.join(parentDir, os.pardir))
	jsonDir = parentDir + '/business.json'
	json_data = open(jsonDir)
	data = json.load(json_data)
	json_data.close()    
	nLinks = len(data)
	start_urls = []
	
	for i in range(nLinks):
		start_urls.append(data[i]["link"][0])

	def parse(self, response):
		sel = Selector(response)
		div = sel.xpath("//div[@class='story-body']")
		#div2 = sel.xpath("//div[@class='emp-description']")
		title = sel.xpath("//h1[@class='story-header']/text()").extract()
		article = ''
		item = ArticleItem()
		# Merge the paragraphs
		for p in div.xpath('.//p/text()'):
			article += p.extract() + ' '
		#for p in div2.xpath('.//p/text()'):
		#	article += p.extract() + ' '
		item['title'] = title
		item['link'] = response.url
		item['article'] = article
		item['subject'] = u'Business'
		return item
		# for url in sel.xpath('//a/@href').extract():
		# 	yield Request(url, callback=self.parse)