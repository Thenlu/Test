# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

# class QichePipeline(object):
#     def process_item(self, item, spider):
#         return item


class QichePipeline(object):
    def process_item(self, item, spider):
        return item
# 写入json文件
# class JsonWritePipline(object):
#     def __init__(self):
#         self.file = open('汽车之家全部型号.json', 'w', encoding='utf-8')
#
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item), ensure_ascii=False) + "\n"
#         self.file.write(line)
#         return item
#
#     def spider_closed(self, spider):
#         self.file.close()


# import pymysql
# def dbHandle():
#     conn = pymysql.connect(
#         host = "localhost",
#         user = "root",
#         passwd = "mysql",
#         charset = "utf8",
#         use_unicode = False
#     )
#     return conn
#
# class QichePipeline(object):
#     def process_item(self,item,spider):
#         dbObject = dbHandle()
#         cursor = dbObject.cursor()
#         cursor.execute("USE car")
#         sql = "INSERT INTO book(author,title,times,url) VALUE (%s,%s,%s,%s)"
#         try:
#             cursor.execute(sql,(item['author'],item['title'],item['times'],item['url']))
#             cursor.connection.commit()
#         except BaseException as e:
#             print("错误在这里>>>>>>>>>>>>>",e,"<<<<<<<<<<<<<错误在这里")
#             dbObject.rollback()
#         return item
