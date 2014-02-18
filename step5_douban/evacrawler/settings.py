#coding=utf-8
import os
try:
   from settings_local import *
except ImportError, e:
   pass


### Scrapy Settings
BOT_NAME = 'evacrawler'

SPIDER_MODULES = ['evacrawler.spiders']
NEWSPIDER_MODULE = 'evacrawler.spiders'

#LOG_LEVEL = 'INFO'

ITEM_PIPELINES = {
    'evacrawler.pipelines.MongoPipeline': 300,
}


DOWNLOAD_DELAY = 0.25

#SPIDER_MIDDLEWARES = {
#    'evacrawler.middlewares.authorization.AuthorizationMiddleware' : 100,
#}

DEFAULT_REQUEST_HEADERS = {
      'Authorization':'Bearer 0391f27d522069160ab5d777f6613b42',
}

COOKIES_DEBUG = True

### Custom Settings

TWITTER = {
    'consumer_key' : '',       
    'consumer_secret' : '',       
    'token_key' : '',       
    'token_secret' : '',       
}

MY_SPIDERS = {
    'wscn_full' : {
        'site_name' : '华尔街见闻',
        'start_url' : ['http://api.wallstreetcn.com/apiv1/node.json'],
        'spider_type' : 'json',
        'depth' : 0,
        'pager_param' : 'page',
        'pager_step' : 1,
        'default_request_headers' : {
            
        },
        'save_collection' : 'wscn',
        'save_db' : 'abc',
    }, 
    'wscn_watcher' : {
        'site_name' : '华尔街见闻',
        'start_url' : ['http://api.wallstreetcn.com/apiv1/node.json'],
        'spider_type' : 'json',
        'depth' : 2,
        'pager_param' : 'page',
        'pager_step' : 1,
        'default_request_headers' : {
            
        }
    }, 
}

MONGODB_SERVER = '192.168.1.12'
MONGODB_PORT = 27017
MONGODB_DB = 'scrapy'
MONGODB_COLLECTION = 'douban'
MONGODB_UNIQ_KEY = '_id'

WORDPRESS_API = 'http://192.168.1.12/wordpress/xmlrpc.php'
WORDPRESS_USER = 'admin' 
WORDPRESS_PASSWORD = '123456'

DOWNLOAD_FILE_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "downloads")

print TWITTER
