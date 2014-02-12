#coding=utf-8
from scrapy.item import Item, Field

class AvnpcPostItem(Item):
    title = Field()
    url = Field()
    content = Field()
