#coding=utf-8
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.spiders import XMLFeedSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import XMLFeedSpider
from scrapy.item import Item
from scrapy.shell import inspect_response
from urlparse import urlparse
from pyquery import PyQuery
from avnpc.items import *
from avnpc import p
import json


class AvnpcRssSpider(XMLFeedSpider):
    name = "rss"
    allowed_domains = ["avnpc.com"]
    start_urls = [
        "http://avnpc.com/feed"
    ]
    namespaces = [('n', 'http://www.w3.org/2005/Atom')]
    #iterator = 'iternodes' 
    iterator = 'xml' 
    itertag = 'n:entry'

    def parse_nodes(self, response, nodes):
        inspect_response(response, self)

    def parse_node(self, response, node):
        p(1)
        item = AvnpcRssItem()
        item['title'] = node.xpath('n:title').extract()
        p(item)
        return item
