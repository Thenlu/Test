import json
import requests
# # url  = "https://rate.tmall.com/list_detail_rate.htm?itemId=527531305749&spuId=513541320&sellerId=2452365526&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvDvvUvbpvUvCkvvvvvjiPPLqpsj1hRFdyzjYHPmPpAj1URssOQjtWP2ShsjDnRphvCvvvvvvPvpvhvv2MMgyCvvOUvvVvaZ8ivpvUvvmvWVp03c%2FtvpvIvvvvbhCvvvvvvU8VphvWQ9vv96CvpC29vvm2phCvhmvvvUnvphvWQ9yCvhQWIJOvC07U%2B8c65E36pf2XS4ZAhjCbFOcnDBvfJ9kx6acEn1vDN%2BLvaNoAdcHCa4AUALutUDJU%2B8c6ei3sod2XS4ZAhjCbFOcnDBmfvphvC9vhvvCvp8wCvvpvvUmm&isg=Au7uNeVSOPwMT0954evIJfZgLUSw77LpDX9VPRi3WvGs-45VgH8C-ZT5x3jK&needFold=0&_ksTS=1512437868617_395&callback=jsonp396"
# url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=541396117031&spuId=128573071&spuId=128573071&sellerId=2616970884&order=3&currentPage=1&append=⊙&content=1'
#
# # url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=541396117031&spuId=128573071&spuId=128573071&sellerId=2616970884&order=3&currentPage=1&append=⊙&content=1'
# req = requests.get(url)
# jsondata = req.text[15:]
# data = json.loads(jsondata)
#
# #输出页面信息
# print('page:',data['paginator']['page'])
# #遍历评论信息列表
# for i in data["rateList"]:
#     #输出商品sku信息
#     print(i['auctionSku'])
#     #输出评论时间和评论内容
#     print(i['rateDate'],i['rateContent'])
#     info = i['appendComment']
#     #判断是否有追加评论
#     if info:
#         print(info['commentTime'])
#         print(info['content'])
#     print('======')

url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=527531305749&sellerId=2452365526&order=3&currentPage=1'
req = requests.get(url)
jsondata = req.text[15:]
data =json.loads(jsondata)

for i in data["rateList"]:
    print(i['auctionSku'])
    print(i['rateContent'])





