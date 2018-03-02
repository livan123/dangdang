# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class DangdangPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host="localhost",
                               user="root",
                               password="123456",
                               db="livan",
                               port=3306,
                               charset='utf8')
        cur = conn.cursor()

        for i in range(0, len(item["title"])):
            title = item["title"][i]
            link = item["link"][i]
            comment = item["comment"][i]
            print(title)
            print(link)
            print(comment)
            sql = "insert into goods(title, link, comment) values('"+title+"','"+link+"','"+comment+"')"
        try:
            cur.execute(sql)
            conn.commit()
        except Exception as e:
            raise e
        finally:
            db.close()  #关闭连接

        return item
