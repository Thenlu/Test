# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    #开始的url从网页上查找规律
    url = "http://hr.tencent.com/position.php?&start="
    #这是url每次点击一次的增加量
    offset = 0
    #需要进行字符串的拼接 完成完整的url  需要进行类型的转换
    start_urls = [url + str(offset)]

    def parse(self, response):
        tr_list = response.xpath("//table[@class='tablelist']/tr")[1:-1]
        for each in tr_list:
            item=TencentItem()
            item["mingcheng"] = each.xpath(".//td[@class='l square']/a/text()").extract_first()
            item["zhiwei"] = each.xpath("./td[2]/text()").extract_first()
            item["number"] = each.xpath("./td[3]/text()").extract_first()
            item["didian"] = each.xpath("./td[4]/text()").extract_first()
            yield item

        if self.offset < 2620:
            self.offset = self.offset + 10

        yield scrapy.Request(self.url + str(self.offset),callback=self.parse)

