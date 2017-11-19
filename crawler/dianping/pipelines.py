# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import MySQLdb
import os
from items import MerchantItem, ClassfyItem, RegionItem

DB_ADDR = os.getenv('DB_PORT_3306_TCP_ADDR', 'localhost')
DB_PORT = int(os.getenv('DB_PORT_3306_TCP_PORT', 3306))
DB_PASSWORD = os.getenv('DB_ENV_MYSQL_ROOT_PASSWORD', '********')


class DianpingPipeline(object):
    def __init__(self):
        self.coon = MySQLdb.connect(host=DB_ADDR, port=DB_PORT, user='root', passwd=DB_PASSWORD, db='dianping',
                                    charset='utf8')

    def process_item(self, item, spider):
        """

        :type item: scrapy.Item
        :rtype: scrapy.Item
        """
        cursor = self.coon.cursor()
        if isinstance(item, MerchantItem):
            sql = "replace into T_merchants(star, name, huanjing, fuwu ,kouwei, tag, ave_price, comment_count, address, img_url, id, detail_url, city, region, classfy) VALUES (%s,%s,%s,%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql,
                           [item['star'], item['name'], item['huanjing'], item['fuwu'], item['kouwei'], item['tag'],
                            item['ave_price'], item['comment_count'], item['address'], item['img_url'], item['id'],
                            item['detail_url'], item['city'], item['region'], item['classfy']])
        elif isinstance(item, ClassfyItem):
            sql = "replace into T_classfy (id, name, parent_id) VALUES (%s,%s, %s)"
            cursor.execute(sql,
                           [item['id'], item['name'], item['parent_id']])
        elif isinstance(item, RegionItem):
            sql = "replace into T_region (id, name, parent_id) VALUES (%s,%s, %s)"
            cursor.execute(sql,
                           [item['id'], item['name'], item['parent_id']])
        self.coon.commit()
        return item

    def close_spider(self, spider):
        self.coon.close()
