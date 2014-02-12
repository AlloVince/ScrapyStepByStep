#coding=utf-8
from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.item import Item
from urlparse import urlparse
from pyquery import PyQuery
from avnpc.items import AvnpcPostItem
from avnpc import p
import json



class AvnpcSpider(CrawlSpider):
    name = "avnpc"
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

        dom = PyQuery(response.body)
        res = []
        item = AvnpcPostItem()
        item['title'] = dom("h1 a").text()
        item['url'] = response.url
        item['content'] = dom('article.typo').html()
        return [item]
