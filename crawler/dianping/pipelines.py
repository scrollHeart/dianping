# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import MySQLdb
import os
from items import MerchantItem

DB_ADDR = os.getenv('DB_PORT_3306_TCP_ADDR', 'localhost')
DB_PORT = int(os.getenv('DB_PORT_3306_TCP_PORT', 3306))
DB_PASSWORD = os.getenv('DB_ENV_MYSQL_ROOT_PASSWORD', '123')

class DianpingPipeline(object):
    def __init__(self):
        self.coon = MySQLdb.connect(host=DB_ADDR, port = DB_PORT, user='root', passwd=DB_PASSWORD, db='dianping', charset='utf8')

    def process_item(self, item, spider):
        """

        :type item: MerchantItem
        :rtype: MerchantItem
        """
        cursor = self.coon.cursor()
        sql = "insert into T_merchants(comment, name, huanjing, fuwu ,kouwei, tag) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,[item['comment'], item['name'], item['huanjing'], item['fuwu'], item['kouwei'], item['tag']])
        self.coon.commit()
        return item

    def close_spider(self, spider):
        self.coon.close()
