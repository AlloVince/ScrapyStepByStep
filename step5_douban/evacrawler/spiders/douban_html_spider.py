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
from evacrawler.items import RelationItem
from evacrawler import p
from scrapy.exceptions import * 
from urllib import quote 
import json
import hashlib


class EvaDoubanSpider(CrawlSpider):
    name = "douban"
    allowed_domains = [
        "douban.com",
        "www.douban.com",
        "movie.douban.com",
    ]
    start_urls = [
        "http://movie.douban.com/mine"
    ]

    rules = [
	        #Rule(SgmlLinkExtractor(allow=('/mine/', )), follow=True, process_request='add_cookie'),
	        Rule(SgmlLinkExtractor(allow=(r'^/people/\w+/collect|wish|do', )), follow=True, process_request='add_cookie', callback='parse_post'),
    ]

    user_id = '1291360'

    user_cookie = 'bid=v7cYWI2VXCI; dbcl2=1291360:tmXVTpZW1iA; push_noty_num=0; push_doumail_num=0; ck=l4FK;'

    def start_requests(self):
        requests = []
        for item in self.start_urls:
            requests.append(Request(url=item, cookies=self.parse_cookie(self.user_cookie)))
        return requests    

    def parse_cookie(self, cookie_string):
        cookie = cookie_string.split(';')
        cookies = {} 
        for i in cookie:
            i = i.rstrip()
            i = i.split('=')
            if len(i) > 1:
                cookies[i[0]] = i[1]
        return cookies


    def add_cookie(self, request):
        request.replace(cookies=self.parse_cookie(self.user_cookie));
        return request;


    def get_user_id(self):
        if self.user_id:
            return self.user_id
        user_id = 0
        self.user_id = user_id
        return user_id

    def parse_post(self, response):
        dom = PyQuery(response.body)
        items = []

        domList = dom('.grid-view .item')
        for domItem in domList.items():
            item = RelationItem()
            item['user_id'] = self.get_user_id()
            item['item_id'] = domItem('.title a').attr('href')
            item['_id'] = hashlib.md5(item['user_id'] + '_' + item['item_id']).hexdigest()
            items.append(item)
        return items
