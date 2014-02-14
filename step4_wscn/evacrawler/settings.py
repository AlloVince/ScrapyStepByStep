#coding=utf-8
import os

### Scrapy Settings
BOT_NAME = 'evacrawler'

SPIDER_MODULES = ['evacrawler.spiders']
NEWSPIDER_MODULE = 'evacrawler.spiders'

#LOG_LEVEL = 'INFO'

ITEM_PIPELINES = {
    'evacrawler.pipelines.MongoPipeline': 300
}


DOWNLOAD_DELAY = 0.5



### Custom Settings

MONGODB_SERVER = '192.168.1.12'
MONGODB_PORT = 27017
MONGODB_DB = 'scrapy'
MONGODB_COLLECTION = 'wscn'
MONGODB_UNIQ_KEY = '_id'

DOWNLOAD_FILE_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "downloads")

