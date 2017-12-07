# -*- coding: utf-8 -*-
import scrapy


class QushiSpider(scrapy.Spider):
    name = 'qushi'
    allowed_domains = ['qushibaike.com']
    box = []
    for num in range(300):
        page = 'https://www.qiushibaike.com/8hr/page/{0}'.format(num)
        box.append(page)
    start_urls = box
    def parse(self, response):
        div_list = response.xpath("//div[@id='content-left']/div")
        # print(div_list,"*"*100)
        for div in div_list:
            item = {}
            item["name"] = div.xpath(".//div[@class='author clearfix']/a[2]/h2/text()").extract_first() #名字
            # print(item)
            item["content"] = div.xpath(".//div[@class = 'content']/span/text()").extract()  #内容
            item["dianzan"] = div.xpath(".//div[@class = 'stats']/span[1]/i/text()").extract() #点赞数量
            item["zhuantai"] = div.xpath(".//div[@class = 'stats']/span[1]/text()").extract()  # 好不好笑
            yield item
        # #获取下一页
        # # next_url = response.xpath("//span[@class='next']/@href")
        # next_url = response.xpath("//ul[@class='pagination']/li[-1]/a/text()")
        # print(next_url,"*"*100)