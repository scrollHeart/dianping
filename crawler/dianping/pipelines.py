# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import MySQLdb
from items import MerchantItem

class DianpingPipeline(object):
    def __init__(self):
        # self.file = open('teacher.json', 'wb')
        self.coon = MySQLdb.connect(host='localhost', user='root', passwd='1234qwer', db='dianping', charset='utf8')


    def process_item(self, item, spider):
        """

        :type item: MerchantItem
        :rtype: MerchantItem
        """
        cursor = self.coon.cursor()
        sql = "insert into T_merchants(comment, name, huanjing, fuwu ,kouwei, tag) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,[item['comment'], item['name'], item['huanjing'], item['fuwu'], item['kouwei'], item['tag']])
        self.coon.commit()
        # content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # self.file.write(content)
        return item

    def close_spider(self, spider):
        self.coon.close()
        # self.file.close()
