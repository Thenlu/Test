# -*- coding: utf-8 -*-
import scrapy
from dongguan.items import DongguanItem

class DgSpider(scrapy.Spider):
    name = 'dg'
    allowed_domains = ['https://www.guazi.com']
    url ="https://www.guazi.com/bj/buy/o"
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        url_list = response.xpath("//ul[@class='carlist clearfix js-top']/li")
        print(url_list,"*"*100)
        #遍历li
        for li in url_list:
            item = DongguanItem()
            # item['carurl'] = li.xpath("")
            #车名
            item['carname'] = li.xpath(".//h2[@class='t']/text()").extract_first()
            #车的日期
            item['date'] = li.xpath(".//div[@class='t-i']/text()").extract()
            # item['licheng'] = li.xpath(".//div[@class='t-i']/text()")
            item['prize'] = li.xpath(".//div[@class='t-price']/p/text()").extract_first()
            item['state'] = li.xpath(".//i[@class='i-orange']/text()").extract_first()
            yield item

            if self.offset <=161:
                self.offset =self.offset + 1

            yield scrapy.Request(self.url + str(self.offset),callback=self.parse)


