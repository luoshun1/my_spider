# -*- coding: utf-8 -*-
import scrapy


class ManhuaduiSpider(scrapy.Spider):
    name = 'manhuadui'
    allowed_domains = ['manhuadui.com']
    start_urls = ['http://manhuadui.com/']

    def parse(self, response):
        pass
