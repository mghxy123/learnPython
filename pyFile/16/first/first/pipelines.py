# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import simplejson as json


class FirstPipeline(object):
    def __init__(self):
        print('{}+++++++++++init++++++++',type(self))

    def open_spider(self, spider):
        print('+'*60)
        print(type(spider), spider.__class__.dict__)
        print(spider.settings.get('filename'))
        self.file = open(spider.settings.get('filename'),'w', encoding='utf-8')
        self.file.write('[\n')

    def close_spider(self, spider):
        # print(type(spider), spider.__class__.__dict__)

        print('-'*60)
        self.file.write(']')
        self.file.close()

    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item))+ ',\n')
        return item
