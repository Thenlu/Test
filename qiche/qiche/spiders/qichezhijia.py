# -*- coding: utf-8 -*-
import scrapy


class QichezhijiaSpider(scrapy.Spider):
    name = 'qichezhijia'
    allowed_domains = ['autohome.com']
    box = []
    for num in range(26):
        page = 'https://www.autohome.com.cn/grade/carhtml/{0}.html'.format(chr(num + ord('A')))
        box.append(page)
    start_urls = box
    def parse(self, response):
        ul_list = response.xpath("//ul[@class='rank-list-ul']/li")
        for li in ul_list:
            item = {}
            item["car_name"] = li.xpath("./h4/a/text()").extract_first()
            item["car_url"] = li.xpath("./h4/a/@href").extract_first()
            item["car_prize"] = li.xpath("./div[1]/a[1]/text()").extract_first()
            if item["car_prize"] == "图库":
                item["car_prize"] = "暂无价格"
            if item["car_prize"] == "报价":
                item["car_prize"] = "暂无价格"
            item["car_koubei"] = li.xpath(".//div[last()]/a[last()]/@href").extract_first()
            yield item
            if item["car_koubei"] is not None:
                url = 'https:'+item["car_koubei"]
                # print(url)

                yield  scrapy.Request(
                    url,
                    callback=self.parsedetail,
                    meta={"item":item}
                )

    def parsedetail(self,response):

        # time.sleep(10)
        print('*'*100)
        item = response.meta["item"]

        # item["car_pingjia"] = response.xpath("//div[@class='revision-impress impress-small']/a[@class=' ']/text()").extract()  #1
        item["car_pingjia"] = response.xpath("//div[revision-impress impress-small']/a/text()").extract()   #2
        yield item

        #revision-impress    or "//div[@class='revision-impress ']/a/text()"


    # https://www.autohome.com.cn/grade/carhtml/A.html

