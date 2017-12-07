# -*- coding: utf-8 -*-
import scrapy
import requests
from lxml import etree
import re


class YykSpider(scrapy.Spider):
    name = 'yyk'
    # name = 'shop'
    allowed_domains = ['tmall.com']
    start_urls = ['https://uniqlo.tmall.com/category.htm']

    def parse(self, response):
        temp_search_url = response.xpath("//input[@id='J_ShopAsynSearchURL']/@value").extract_first()
        # 处理starturl，获取url地址的前部分url
        temp_url = requests.utils.urlparse(response.request.url)
        # 详情页的url的地址
        search_url = temp_url.scheme + "://" + temp_url.netloc + temp_search_url
        print(search_url, "*" * 100)
        yield scrapy.Request(
            search_url,
            callback=self.parse_product_list
        )

    def parse_product_list(self, response):  # 真正的详情页的response的解析
        html_str = response.body.decode("gbk")  #
        html_str = re.sub(r"\\", "", html_str)
        html = etree.HTML(html_str)

        # with open("tmall1.html","w",encoding="gbk") as f:
        #     f.write(etree.tostring(html).decode("gbk"))
        dl_list = html.xpath("//div[@class='J_TItems']/div[position()<=8]/dl")  # 列表页
        # dl_list = html.xpath("//dl[@class='item ']")
        # print(dl_list,"-"*100)
        for dl in dl_list:
            item = {}
            item["item_name"] = dl.xpath(".//dd[@class='detail']/a/text()")[0]
            item["item_href"] = "https:" + dl.xpath(".//dd[@class='detail']/a/@href")[0]
            item["item_price"] = dl.xpath(".//span[@class='c-price']/text()")[0]
            item["sale_num"] = dl.xpath(".//span[@class='sale-num']/text()")[0]
            item["comments_num"] = dl.xpath("./dd[@class='rates']//h4/a/span/text()")
            item["comments_num"] = item["comments_num"][0] if len(item["comments_num"]) > 0 else None
            print(item, "-" * 100)

        # 翻页
        next_url_temp = html.xpath("//a[@class='J_SearchAsync next']/@href")
        print(next_url_temp, "=" * 100)
        next_url = "https:" + next_url_temp[0] if len(next_url_temp) > 0 else None
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse  # 下一页的url地址也是和前面的一样
            )
