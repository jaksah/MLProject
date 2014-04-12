# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class NewsItem(Item):
    # define the fields for your item here like:
    # name = Field()
    title = Field()
    link = Field()
    description = Field()
    subject = Field()
    # pass
