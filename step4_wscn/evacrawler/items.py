#coding=utf-8
from scrapy.item import Item, Field

class ArticleItem(Item):
    title = Field()
    url = Field()
    author = Field()
    update_time = Field()
    content = Field()
