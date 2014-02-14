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




### Custom Settings

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'scrapy'
MONGODB_COLLECTION = 'person_profiles'
MONGODB_UNIQ_KEY = '_id'

DOWNLOAD_FILE_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "downloads")

