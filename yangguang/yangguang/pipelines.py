# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import re
import json

from pymongo import MongoClient

logger = logging.getLogger(__name__)


class YangguangPipeline(object):
    def open_spider(self, spider):
        client = MongoClient()
        self.collection = client["MySpider"]["yangguang"]

    def close_spider(self, spider):
        logger.warning(self.collection.find_one())

    def process_item(self, item, spider): # spider:当前要处理的spider对象
        # if spider.name == 'yg':
        #     logger.warning('*'*100)
        item["content"] = self.process_content(item["content"])
        # logger.warning(item)
        # self.collection.insert(dict(item))
        return item

    def process_content(self, content):
        content = [re.sub(r"\xa0|\s", "", i) for i in content]
        content = [i for i in content if len(i)>0]
        return content
