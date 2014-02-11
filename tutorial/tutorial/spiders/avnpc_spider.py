from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from urlparse import urlparse
from tutorial  import p



class AvnpcSpider(BaseSpider):
    name = "avnpc"
    allowed_domains = ["avnpc.com"]
    start_urls = [
        "http://avnpc.com/"
    ]

    def parse(self, response):
        url = urlparse(response.url)
        filename = 'index.html' if url.path == '/' else url.path.split("/")[-1] + '.html'
        open(filename, 'wb').write(response.body)
