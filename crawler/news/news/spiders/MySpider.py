from scrapy import log
from scrapy.contrib.spiders import XMLFeedSpider
from news.items import NewsItem

class MySpider(XMLFeedSpider):
    name = 'bbcfeed'
    allowed_domains = ['feeds.bbci.co.uk/']
    start_urls = ['http://feeds.bbci.co.uk/sport/0/rss.xml']
    iterator = 'iternodes' # This is actually unnecessary, since it's the default value
    itertag = 'item'	

    def parse_node(self, response, node):
        log.msg('Hi, this is a <%s> node!: %s' % (self.itertag, ''.join(node.extract())))

        item = NewsItem()
        item['title'] = node.xpath('title/text()').extract()
        item['link'] = node.xpath('link/text()').extract()
        item['description'] = node.xpath('description/text()').extract()
        item['subject'] = [u"Sports"]

        # print('Extracted information:')
        # print item['title'][0]
        # print item['link'][0]
        # print item['description'][0]
        # print item['subject'][0]

        #print item

        return item