# -*- coding: utf-8 -*-
import logging

import scrapy


logger = logging.getLogger(__name__)


class Itcast1Spider(scrapy.Spider):
    name = 'itcast1'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/']

    def parse(self, response):
        item = {}
        item['come_from'] = "itcast"
        logger.warning(item)
        yield item
