#coding=utf-8
import os
import json
import codecs 
from urlparse import urlparse
from scrapy.exceptions import * 
from evacrawler.items import *
from evacrawler import *
from scrapy.conf import settings
from scrapy import log
import wordpresslib


class MongoPipeline(object):
    def __init__(self):
        import pymongo
        connection = pymongo.Connection(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        self.db = connection[settings['MONGODB_DB']]
        self.collection = self.db[settings['MONGODB_COLLECTION']]
        if self.__get_uniq_key() is not None:
            self.collection.create_index(self.__get_uniq_key(), unique=True)

    def process_item(self, item, spider):
        if self.__get_uniq_key() is None:
            self.collection.insert(dict(item))
        else:
            self.collection.update(
                            {self.__get_uniq_key(): item[self.__get_uniq_key()]},
                            dict(item),
                            upsert=True)  
        log.msg("Item wrote to MongoDB database %s/%s" %
                    (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
                    level=log.DEBUG, spider=spider)  
        return item

    def __get_uniq_key(self):
        if not settings['MONGODB_UNIQ_KEY'] or settings['MONGODB_UNIQ_KEY'] == "":
            return None
        return settings['MONGODB_UNIQ_KEY']

class WordPressPipeline(object):
    def __init__(self):
        self.rpc = wordpresslib.WordPressClient(settings['WORDPRESS_API'], settings['WORDPRESS_USER'], settings['WORDPRESS_PASSWORD'])

    def process_item(self, item, spider):
        self.rpc.selectBlog(0)
        article = item['raw']
        post = wordpresslib.WordPressPost()
        post.title = article['title']
        post.description = article['body']['und'][0]['safe_value'] 
        idPost = self.rpc.newPost(post, True)
        return item


class FilePipeline(object):
    def process_item(self, item, spider):
        url = urlparse(item['url'].rstrip('/'))
        filename = 'index.json' if url.path == '/' else url.path.split("/")[-1] + '.json'
        #filepath = os.path.dirname(__file__) + '/../download/' + filename
        filepath = settings['DOWNLOAD_FILE_FOLDER'] + '/' + filename
        
        codecs.open(filepath, 'wb', encoding='utf-8').write(json.dumps(dict(item), ensure_ascii=False))
        #raise CloseSpider('exit')
        return item
