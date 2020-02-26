# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import os


class AnimespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class JSONPipeline(object):
    """
        导出JSON格式
    """
    def __init__(self):
        self.file = None
        self.jsonpath = os.path.dirname(__file__) + '/spiders/output'


    def process_item(self, item, spider):
        self.file = codecs.open('%s/%s_items.json' % (self.jsonpath, spider.name), 'a', encoding='utf-8')
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
