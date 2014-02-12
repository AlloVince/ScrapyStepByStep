#coding=utf-8
BOT_NAME = 'avnpc'

SPIDER_MODULES = ['avnpc.spiders']
NEWSPIDER_MODULE = 'avnpc.spiders'

ITEM_PIPELINES = {
    'avnpc.pipelines.AvnpcPipeline': 300
}
