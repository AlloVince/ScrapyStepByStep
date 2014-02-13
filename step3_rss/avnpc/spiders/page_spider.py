#coding=utf-8
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.spiders import XMLFeedSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import XMLFeedSpider
from scrapy.item import Item
from urlparse import urlparse
from pyquery import PyQuery
from avnpc.items import *
from avnpc import p
import json
from readability.readability import Document
import urllib
import codecs



class AvnpcPostSpider(CrawlSpider):
    name = "page"
    allowed_domains = ["avnpc.com"]
    start_urls = [
        "http://avnpc.com/"
    ]

    rules = [
	        Rule(SgmlLinkExtractor(allow=('/pages/.*', )), follow=True, callback='parse_post')
    ]

    def add_cookie(self, request):
        request.replace(cookies=[
        ]);
        return request;


    def parse_post(self, response):
    #def parse(self, response):

        dom = PyQuery(response.body)
        res = []
        item = AvnpcPostItem()
        item['title'] = Document(response.body).summary()
        item['url'] = response.url
        item['content'] = Document(response.body).summary()
        return [item]
