# -*- coding: utf-8 -*-
# 商户的爬虫
import sys

import re

reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
from dianping.items import MerchantItem


class MerchantsSpider(scrapy.Spider):
    name = "merchants"
    allowed_domains = ["dianping.com"]
    start_urls = ['http://www.dianping.com/search/category/3/10/g112o3p1']

    def parse(self, response):
        with open('test.html', 'w') as f:
            f.write(response.text.encode('utf-8'))

        items = []
        # //*[@id="shop-all-list"]/ul/li/div[2]/div[1]/a/h4
        node = response.xpath('//*[@id="shop-all-list"]/ul/li')
        for each in node:
            item = MerchantItem()
            item['name'] = each.xpath('div[2]/div[1]/a/h4/text()').extract()[0]
            item['comment'] = each.xpath('div[2]/div[2]/span[1]/@title').extract()[0]
            item['kouwei'] = each.xpath('div[2]/span[1]/span[1]/b/text()').extract()[0]
            item['huanjing'] = each.xpath('div[2]/span[1]/span[2]/b/text()').extract()[0]
            item['fuwu'] = each.xpath('div[2]/span[1]/span[3]/b/text()').extract()[0]
            item['tag'] = each.xpath('div[2]/div[3]/a[1]/span/text()').extract()[0]

            items.append(item)

            curpage = re.search('p(\d+)', response.url).group(1)
            page = int(curpage) + 1
            url = re.sub('p(\d+)', 'p' + str(page), response.url)

            # 发送新的url请求加入待爬队列，并调用回调函数 self.parse
            yield scrapy.Request(url, callback=self.parse)

            yield item
