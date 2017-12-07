# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class JianshuPipeline(object):
#     def process_item(self, item, spider):
#         return item

import pymysql
def dbHandle():
    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        passwd = "mysql",
        charset = "utf8",
        use_unicode = False
    )
    return conn

class JianshuPipeline(object):
    def process_item(self,item,spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        cursor.execute("USE testdb")
        sql = "INSERT INTO book(author,title,times,url) VALUE (%s,%s,%s,%s)"
        try:
            cursor.execute(sql,(item['author'],item['title'],item['times'],item['url']))
            cursor.connection.commit()
        except BaseException as e:
            print("错误在这里>>>>>>>>>>>>>",e,"<<<<<<<<<<<<<错误在这里")
            dbObject.rollback()
        return item



# #导入pymysql模块
# import pymysql
# #连接数据库
# conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='music')
# cur = conn.cursor()
# #输入使用数据库和查询信息的命令，操作类似在cmd中的输入
# cur.execute("USE music")
# #插入数据(pages是数据库music下的表)
# cur.execute("INSERT INTO pages(title,content) VALUES('449454051','http://m2.music.126.net/GvSlxgdwVCKelv3gFaw9pg==/18641120138988064.mp3')")
# cur.connection.commit()
# #更新数据
# cur.execute("SELECT * FROM pages")
# print("获取全部信息\n",cur.fetchall())
# #关闭数据库
# cur.close()
# conn.close()














