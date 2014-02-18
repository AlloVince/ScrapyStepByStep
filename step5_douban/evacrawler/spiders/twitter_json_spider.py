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
from scrapy.conf import settings
import json
import hashlib
import oauth2 as oauth
import urllib


class TwitterJsonSpider(BaseSpider):
    name = "twitter"
    allowed_domains = ["twitter.com"]
    start_urls = [
        "https://api.twitter.com/1.1/statuses/user_timeline.json"
    ]

    oauth_headers = {} 

    def get_oauth_headers(self):
        if self.oauth_headers:
            return self.oauth_headers

        p(settings['TWITTER'])

        headers = {}
        return headers

    def start_requests(self):
        requests = []
        for item in self.start_urls:
            requests.append(Request(url=item, headers=self.get_oauth_headers()))
        return requests


    def parse(self, response):
        res = json.loads(response.body)

        if not res:
            raise CloseSpider('Scrawl finished')

        p(res)
        '''
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
        '''

    def parse_subject(self, response):
        item = ArticleItem()
        subject = json.loads(response.body)
        item['raw'] = subject
        item['_id'] = hashlib.md5(response.url).hexdigest()
        return [item]
