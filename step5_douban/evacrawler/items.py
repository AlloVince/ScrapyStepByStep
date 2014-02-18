#coding=utf-8
from scrapy.item import Item, Field

class RelationItem(Item):
    _id = Field()
    user_id = Field()
    item_id = Field()

class ArticleItem(Item):
    _id = Field()
    title = Field()
    url = Field()
    author = Field()
    update_time = Field()
    content = Field()
    raw = Field()
