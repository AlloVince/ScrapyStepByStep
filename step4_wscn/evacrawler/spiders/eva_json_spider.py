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


class EvaJsonSpider(BaseSpider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = [
        "http://api.douban.com/v2/movie/top250"
    ]
    def parse(self, response):
        res = json.loads(response.body)

        if not res['subjects']:
            raise CloseSpider('Scrawl finished')

        for subject in res['subjects']:
            url = 'http://api.douban.com/v2/movie/subject/' + subject['id']
            yield Request(url, callback=self.parse_subject)
        
        next_page = list(urlparse.urlparse(response.url))
        count = res['count']
        if next_page[4]:
            query = dict(urlparse.parse_qs(next_page[4]))
            query['start'] = int(query['start'][0]) + count
        else:
            query = {'start' : count}
            
        next_page[4] = urllib.urlencode(query)
        next_page = urlparse.urlunparse(next_page)
        yield Request(next_page, callback=self.parse)

    def parse_subject(self, response):
        item = ArticleItem()
        subject = json.loads(response.body)
        item['title'] = subject['title']
        item['url'] = response.url
        return [item]
