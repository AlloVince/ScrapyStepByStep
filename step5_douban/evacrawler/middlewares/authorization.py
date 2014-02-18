#coding=utf-8
from scrapy.http import Request
from scrapy.exceptions import NotConfigured
from evacrawler import p

class AuthorizationMiddleware(object):
    def process_start_requests(self, start_requests, spider):
        return [start_requests]
