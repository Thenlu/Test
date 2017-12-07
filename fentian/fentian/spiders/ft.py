# -*- coding: utf-8 -*-
import scrapy
import time
import json
from copy import deepcopy
class FtSpider(scrapy.Spider):
    name = 'ft'
    allowed_domains = ['www.tmall.com','list.tmall.com','detail.tmall.com','rate.tmall.com']
    box = ['https://list.tmall.com/search_shopitem.htm?spm=a220m.1000858.1000725.2.4804c8988CsbUq&user_id=2452365526&from=_1_&stype=search']
           # 'https://list.tmall.com/search_shopitem.htm?spm=a220m.1000862.0.0.2ba5d091KYro1V&s=60&style=sg&sort=s&user_id=2452365526&from=_1_&stype=search#grid-column',
           # 'https://list.tmall.com/search_shopitem.htm?spm=a220m.1000862.0.0.6e09b71bJGjDJN&s=120&style=sg&sort=s&user_id=2452365526&from=_1_&stype=search#grid-column']
    # start_urls = ['https://list.tmall.com/search_shopitem.htm?spm=a220m.1000862.0.0.6e52d5d6jyChj9&style=sg&sort=s&user_id=2452365526&from=_1_&stype=search']
    # for page in box:
    start_urls = box

    def parse(self, response):
        div_list = response.xpath("//div[@class='view grid-nosku']/div")
        # print(div_list,"*"*100)
        item={}
        for div in div_list:
            item["name"] = div.xpath(".//p[@class='productTitle']/a/text()").extract_first()
            item["prize"] = div.xpath(".//p[@class='productPrice']/em/text()").extract_first()
            item["car_href"] = 'http:' + div.xpath(".//div[@class='productImg-wrap']/a/@href").extract_first()
            item["stat"] = div.xpath(".//p[@class='productStatus']/span/em/text()").extract()
            # item["pc_name"] =
            #请求里面的链接
            # print(item["car_href"])
            # time.sleep(3)
            yield item["name"],item["prize"],item["car_href"],item["stat"]
            yield scrapy.Request(
                item["car_href"],
                callback=self.parse_url,
                meta={"item":deepcopy(item)}

            )
            #网站下一页的拼接
            offset = 0
            while offset <= 120:
                offset = offset + 60
                next_url = "https://list.tmall.com/search_shopitem.htm?s={0}&style=sg&sort=s&user_id=2452365526&from=_1_&stype=search#grid-column".format(offset)
                yield scrapy.Request(

                    next_url,
                    callback=self.parse
                )

    # 找到json 的url 地址
    def parse_url(self,response):
        item=deepcopy(response.meta["item"])
        #店铺ID
        item["store_num"] = response.xpath("//div[@id='LineZing']/@itemid").extract_first()
        item["shop_num"] = response.xpath("//div[@id='shop-info']/div/input[2]/@value").extract_first()
        # print(item["store_num"],"a"*100)
        # print(item["shop_num"],"b"*100)

        if item["store_num"] and item["shop_num"] is not None:
            item["json_url"] = "https://rate.tmall.com/list_detail_rate.htm?itemId={0}&sellerId={1}&order=3&currentPage=1".format(item["store_num"],item["shop_num"])
        if item["json_url"] is not None:
            # json_url = "https://rate.tmall.com/list_detail_rate.htm?itemId={0}&sellerId={1}&order=3&currentPage=1".format(item["store_num"],item["shop_num"])
            # print(json_url,"/"*100)
            yield scrapy.Request(
                item["json_url"],
                callback=self.parse_pinglun,
                meta={"item": deepcopy(item)},

                # meta={"item": deepcopy(item)}
            )
        # if item["pc_pingjia"] ==0:

        # if item["json_url"] == "https://rate.tmall.com/list_detail_rate.htm?itemId={0}&sellerId={1}&order=3&currentPage=0".format(item["store_num"],item["shop_num"]):

            # item["json_url"] = "暂时没有评论"

    # #拿到详情页的地址进去获取评论
    def parse_pinglun(self,response):

        item=deepcopy(response.meta["item"])  #用来接受数据
        print("-",*"100")
        #解码
        ret = response.text[15:]
        #吧json格式的数据转换为python格式，
        rate=json.loads(ret)
        if rate["rateList"]:
            for i in rate["rateList"]:
                item["pc_name"] = i['displayUserNick']
                item["pc_pingjia"] = i['rateContent']
                yield item
        else:
            item["pc_pingjia"] ='暂无评价'
            yield item



                        # rate = rate["rateList"][0]["rateContent"]
        # print(rate,"="*100)
        # for i in rate["rateList"]:
        #     print(i['displayUserNick'])
        #     print(i['rateContent'])




























    #     #遍历
    #     for each in rateList:
    #         #这是买家
    #         item["displayUserNick"] = each["displayUserNick"]
    #         #这是评论
    #         item["rateContent"] = each["rateContent"]
    #         #这是时间
    #         item["rateDate"] = each["rateDate"]
    #         yield item
    #
    #         #评论的url
    #
    #         yield scrapy.Request("https://rate.tmall.com/list_detail_rate.htm?itemId=553270584379&spuId=857010874&sellerId=2452365526&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hv")
    #         # def pageparse(self,response):
    #         #     pass



