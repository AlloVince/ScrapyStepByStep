#coding=utf-8
from scrapy.contrib.spiders import *
from scrapy.spider import BaseSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import XMLFeedSpider
from scrapy.item import Item
from scrapy.shell import inspect_response
from scrapy.http import Request
import urlparse
from pyquery import PyQuery
from evacrawler.items import *
from evacrawler import p
from scrapy.exceptions import * 
import urllib
import json
import hashlib


class EvaJsonSpider(BaseSpider):
    name = "wscn"
    allowed_domains = ["wallstreetcn.com"]
    start_urls = [
        "http://api.wallstreetcn.com/apiv1/node.json"
    ]
    def parse(self, response):
        res = json.loads(response.body)

        if not res:
            raise CloseSpider('Scrawl finished')

        for subject in res:
            url = subject['uri'] + '.json'
            yield Request(url, callback=self.parse_subject)
        
        next_page = list(urlparse.urlparse(response.url))
        if next_page[4]:
            query = dict(urlparse.parse_qs(next_page[4]))
            query['page'] = int(query['page'][0]) + 1
        else:
            query = {'page' : 1}
            
        next_page[4] = urllib.urlencode(query)
        next_page = urlparse.urlunparse(next_page)
        yield Request(next_page, callback=self.parse)

    def parse_subject(self, response):
        item = ArticleItem()
        subject = json.loads(response.body)
        item['title'] = subject['title']
        item['url'] = response.url
        item['raw'] = subject
        item['_id'] = hashlib.md5(response.url).hexdigest()
        return [item]
