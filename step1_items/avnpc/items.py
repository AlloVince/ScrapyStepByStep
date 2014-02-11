from scrapy.item import Item, Field

class AvnpcItem(Item):
    title = Field()
    url = Field()
