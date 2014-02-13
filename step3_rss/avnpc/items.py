#coding=utf-8
from scrapy.item import Item, Field

class AvnpcPostItem(Item):
    title = Field()
    url = Field()
    update_time = Field()
    content = Field()

class AvnpcRssItem(Item):
    title = Field()
    url = Field()
    update_time = Field()
    content = Field()
