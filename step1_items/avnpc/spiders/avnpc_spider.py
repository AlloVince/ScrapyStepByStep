from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from urlparse import urlparse
from pyquery import PyQuery
from avnpc.items import AvnpcItem
from avnpc import p
import json



class AvnpcSpider(BaseSpider):
    name = "avnpc"
    allowed_domains = ["avnpc.com"]
    start_urls = [
        "http://avnpc.com/"
    ]

    def parse(self, response):
        url = urlparse(response.url)
        filename = 'index.json' if url.path == '/' else url.path.split("/")[-1] + '.json'
        
        dom = PyQuery(response.body)
        items = []
        res = []
        for post in dom.items('h3 a'):
            item = AvnpcItem()
            item['title'] = post.text()
            item['url'] = post.attr("href")
            items.append(item)
        #open(filename, 'wb').write(json.dumps(res))
        return items
