# -*- coding: utf-8 -*-
# 商户的爬虫
import sys
import re
import scrapy
import itertools
import MySQLdb
from dianping.items import MerchantItem
from dianping.Util import getXpathFirst
from dianping.pipelines import DB_ADDR, DB_PORT, DB_PASSWORD

city = '3'
cate = '10'

BASE_URL = 'http://www.dianping.com/search/category/{city}/{cate}/'.format(city=city, cate=cate)

def crawUrls():
    coon = MySQLdb.connect(host=DB_ADDR, port=DB_PORT, user='root', passwd=DB_PASSWORD, db='dianping',
                                charset='utf8')
    cursor = coon.cursor()
    sql = 'SELECT id FROM T_classfy;'
    cursor.execute(sql)
    classfy_result = [item[0] for item in  cursor.fetchall()]

    sql = 'SELECT id FROM T_region;'
    cursor.execute(sql)
    region_result = [item[0] for item in cursor.fetchall()]
    urls = []
    for item in itertools.product(classfy_result, region_result):
        url = BASE_URL + item[0] + item[1] + 'p1'
        urls.append(url)
    coon.commit()
    coon.close()
    return urls

class MerchantsSpider(scrapy.Spider):
    name = "merchants"
    allowed_domains = ["dianping.com"]
    #  查询数据库中的classfy和region两张表，用这两张表，拼接成url，然后添加到start_urls中
    start_urls = crawUrls()

    def parse(self, response):
        with open('{}.html'.format(self.name), 'w') as f:
            f.write(response.text.encode('utf-8'))

        items = []
        # //*[@id="shop-all-list"]/ul/li/div[2]/div[1]/a/h4
        node = response.xpath('//*[@id="shop-all-list"]/ul/li')
        for each in node:
            item = MerchantItem()
            item['name'] = getXpathFirst(each.xpath('div[2]/div[1]/a/h4/text()').extract())
            item['star'] = getXpathFirst(each.xpath('div[2]/div[2]/span[1]/@title').extract(), None)
            item['kouwei'] = getXpathFirst(each.xpath('div[2]/span[1]/span[1]/b/text()').extract(), 0)
            item['huanjing'] = getXpathFirst(each.xpath('div[2]/span[1]/span[2]/b/text()').extract(), 0)
            item['fuwu'] = getXpathFirst(each.xpath('div[2]/span[1]/span[3]/b/text()').extract(), 0)
            item['tag'] = getXpathFirst(each.xpath('div[2]/div[3]/a[1]/span/text()').extract(), None)

            ave_price = getXpathFirst(each.xpath('div[2]/div[2]/a[2]/b/text()').extract(), '0')
            item['ave_price'] = re.search(r'(\d+)', ave_price).group(1)
            item['comment_count'] = getXpathFirst(each.xpath('div[2]/div[2]/a[1]/b/text()').extract(), 0)
            item['address'] = getXpathFirst(each.xpath('div[2]/div[3]/span/text()').extract(), None)
            item['img_url'] = getXpathFirst(each.xpath('div[1]/a/img/@data-src').extract(), '')
            shop_url = getXpathFirst(each.xpath('div[2]/div[1]/a/@href').extract(), None)
            item['detail_url'] = shop_url
            if shop_url:
                item['id'] = shop_url.split('/')[-1]

            item['city'] = city
            print response.url
            result = re.search(r'/(\w\d+)(\w\d+)p(\d+)', response.url)

            print result.group()

            item['classfy'] = result.group(1)
            item['region'] = result.group(2)
            curpage = result.group(3)
            items.append(item)

            page = int(curpage) + 1
            url = re.sub('p(\d+)', 'p' + str(page), response.url)

            # 发送新的url请求加入待爬队列，并调用回调函数 self.parse
            # if page <10 :
            yield scrapy.Request(url, callback=self.parse)

            yield item
