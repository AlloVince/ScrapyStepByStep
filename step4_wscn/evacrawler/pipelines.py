#coding=utf-8
import os
import json
import codecs 
from urlparse import urlparse
from scrapy.exceptions import * 
from evacrawler.items import *
from evacrawler import *
from scrapy.conf import settings


class MongoPipeline(object):
    def process_item(self, item, spider):
        url = urlparse(item['url'].rstrip('/'))
        filename = 'index.json' if url.path == '/' else url.path.split("/")[-1] + '.json'
        #filepath = os.path.dirname(__file__) + '/../download/' + filename
        filepath = settings['DOWNLOAD_FILE_FOLDER'] + '/' + filename
        
        codecs.open(filepath, 'wb', encoding='utf-8').write(json.dumps(dict(item), ensure_ascii=False))
        #raise CloseSpider('exit')
        return item
