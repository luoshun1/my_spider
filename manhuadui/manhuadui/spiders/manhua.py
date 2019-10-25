# -*- coding: utf-8 -*-
import scrapy


class ManhuaSpider(scrapy.Spider):
    name = 'manhua'
    allowed_domains = ['manhuadui.com']
    start_urls = ['http://manhuadui.com/']

    def parse(self, response):
        pass
