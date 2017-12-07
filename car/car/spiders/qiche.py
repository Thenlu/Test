# -*- coding: utf-8 -*-
import scrapy


class QicheSpider(scrapy.Spider):
    name = 'qiche'
    allowed_domains = ['k.autohome.com.cn']
    start_urls = ['http://k.autohome.com.cn/']

    def parse(self, response):
        pass
