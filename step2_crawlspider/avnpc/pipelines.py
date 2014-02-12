#coding=utf-8
import json
import codecs 
from urlparse import urlparse
from scrapy.exceptions import * 
from avnpc.items import AvnpcPostItem
from avnpc import *

class AvnpcPipeline(object):
    def process_item(self, item, spider):
        url = urlparse(item['url'].rstrip('/'))
        filename = 'index.json' if url.path == '/' else url.path.split("/")[-1] + '.json'
        codecs.open(filename, 'wb', encoding='utf-8').write(json.dumps(dict(item), ensure_ascii=False))
        #raise CloseSpider('exit')
        return item
