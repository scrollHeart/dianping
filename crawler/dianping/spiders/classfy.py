# -*- coding: utf-8 -*-
import re

import scrapy

from dianping.Util import getXpathFirst
from dianping.items import ClassfyItem, RegionItem


class ClassfySpider(scrapy.Spider):
    name = "classfy"
    allowed_domains = ["dianping.com"]
    start_urls = ['http://www.dianping.com/search/category/3/10']

    def parse(self, response):
        with open('{}.html'.format(self.name), 'w') as f:
            f.write(response.text.encode('utf-8'))

        items = []
        node = response.xpath('//*[@id="classfy"]/a')
        for each in node:
            item = ClassfyItem()
            url = getXpathFirst(each.xpath('@href').extract(), '')
            item['id'] = url.split('/')[-1]
            item['name'] = getXpathFirst(each.xpath('span/text()').extract(), '')
            item['parent_id'] = re.search(r'category/\d+/(\d+)', response.url).group(1)
            items.append(item)
            # 发送新的url请求加入待爬队列，并调用回调函数 self.parse
            yield scrapy.Request(url, callback=self.parse)
            if item['name'] == '不限':
                continue
            yield item

        items = []
        node = response.xpath('//*[@id="classfy-sub"]/a')
        for each in node:
            item = ClassfyItem()
            item['id'] = getXpathFirst(each.xpath('@href').extract(), '').split('/')[-1]
            item['name'] = getXpathFirst(each.xpath('span/text()').extract(), '')
            item['parent_id'] = response.url.split('/')[-1]
            items.append(item)
            if item['name'] == '不限':
                continue
            yield item
