#coding=utf-8
BOT_NAME = 'avnpc'

SPIDER_MODULES = ['avnpc.spiders']
NEWSPIDER_MODULE = 'avnpc.spiders'

#LOG_LEVEL = 'INFO'

ITEM_PIPELINES = {
    'avnpc.pipelines.AvnpcPipeline': 300
}
