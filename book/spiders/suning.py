# -*- coding: utf-8 -*-
import scrapy
import re
from copy import deepcopy
class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['http://snbook.suning.com/web/trd-fl/999999/0.htm']

    def parse(self, response):
        li_list = response.xpath("//ul[@class='ulwrap']/li")
        # print(li_list,"*"*100)
        for li in li_list:
            item={}
            # print(item,)
            item["b_cate"]=li.xpath("./div[1]/a/text()").extract_first()
            a_list = li.xpath("./div[2]/a")
            #获取小分类 遍历小分类
            for a in a_list:
                item["s_cate"] = a.xpath("./text()").extract_first()
                item["s_href"] = "http://snbook.suning.com/"+a.xpath("./@href").extract_first()
                yield scrapy.Request(
                    item["s_href"],
                    callback=self.parse_book_list,
                    meta={"item":deepcopy(item)}
                )


    def parse_book_list(self,response):
        item = response.meta["item"]
        li_list = response.xpath("//div[@class='filtrate-books list-filtrate-books']/ul/li")
        for li in li_list:
            item["book_img"] = li.xpath("./div[@class='book-img']/a/img/@src").extract_first()
            item["book_title"] = li.xpath(".//div[@class='book-title']/a/@title").extract_first()
            item["book_publish"] = li.xpath(".//div[@class ='book-publish']/a/text()").extract_first()
            item["book_desc"] = li.xpath(".//div[@class='book-descrip c6']/text()").extract_first()
            item["book_href"] = li.xpath("./div[@class='book-img']/a/@href").extract_first()

            yield scrapy.Request(
                item["book_href"],
                callback=self.parse_book_detail,
                meta={"item":deepcopy(item)}
            )
    def parse_book_detail(self,response):
        item = response.meta["item"]
        ret = re.findall(r"'\'bp\':'(.*?)',",response.body.decode(),re.S)
        print(item)