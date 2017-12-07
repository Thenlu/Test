# -*- coding: utf-8 -*-
import scrapy
import re

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/327550029/profile']
    cookies = "anonymid=j3jxk555-nrn0wh; _r01_=1; rechargeuid=327550029; renrenuid=327550029; _ga=GA1.2.1274811859.1497951251; depovince=BJ; jebecookies=c575b937-6610-4a5e-b26d-8699db41cf21|||||; JSESSIONID=abcrDFDFdIrvSdODPep_v; ick_login=c358484b-3ed8-47e8-97ed-2fabc31cbeb8; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=2a941db56cbc616a320391f0ac1fe0169; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20171104/1435/original_UqRN_aeb20000a1aa1986.jpg; t=7129aba283105153008034c5faae4fb89; societyguester=7129aba283105153008034c5faae4fb89; id=327550029; xnsid=70ed44e9; loginfrom=syshome; ch_id=10016; wp_fold=0"
    cookies = {i.split("=")[0]:i.split("=")[-1] for i in cookies.split("; ")}

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                callback=self.parse,
                cookies=self.cookies
            )
    def parse(self, response):
        print(re.findall("毛兆军",response.body.decode(),re.S))
        yield scrapy.Request(
            "http://www.renren.com/327550029/profile?v=info_timeline",
            callback=self.parse2,
        )
    def parse2(self,response):
        print(re.findall("毛兆军", response.body.decode(), re.S))