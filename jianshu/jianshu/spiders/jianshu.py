# -*- coding: utf-8 -*-
import scrapy

class JianshuSpider(scrapy.Spider):
    name = 'jianshu'
    box = []
    for num in range(120):
        pages = 'http://www.jianshu.com/c/V2CqjW?order_by=commented_at&page={0}'.format(num)
        box.append(pages)
    start_urls = box
    def parse(self, response):
        item = {}
        articles = response.xpath("//ul[@class='note-list']/li")
        # print(articles,"*"*100)
        for article in articles:
            item['author'] = article.xpath('.//div[@class="info"]/a/text()').extract_first() #作者
            item['title'] = article.xpath('.//a[@class="title"]/text()').extract_first() #标题
            item['times'] = article.xpath('.//span[@class="time"]/@data-shared-at').extract_first() #时间
            url = article.xpath('.//div[@class="content"]/a/@href').extract_first()
            item['url'] = 'http://www.jianshu.com' + url
            # admire = article.xpath('.//div/div[2]/span[2]/text()').extract()
            # item['admire'] = ''.join(admire)
            # likes = article.xpath('.//div/div[2]/span[1]/text()').extract()
            # item['likes'] = ''.join(likes)
            yield item
            # print(item)
