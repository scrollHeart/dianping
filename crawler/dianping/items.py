# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MerchantItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  # 名称
    star = scrapy.Field()  # 星级
    kouwei = scrapy.Field()  # 口味评分
    huanjing = scrapy.Field()  # 环境评分
    fuwu = scrapy.Field()  # 服务评分
    tag = scrapy.Field()  # 分类

    ave_price = scrapy.Field()  # 平均价格
    comment_count = scrapy.Field()  # 评论数
    phone = scrapy.Field()  # 电话
    address = scrapy.Field()  # 地址
    img_url = scrapy.Field()  # 地址
    detail_url = scrapy.Field()  # 地址
    id = scrapy.Field()  # 商户id

    city = scrapy.Field()
    region = scrapy.Field()
    classfy = scrapy.Field()

class ClassfyItem(scrapy.Item):
    name = scrapy.Field()    # 分类名
    id = scrapy.Field()     # id，例如麻辣烫： g221
    parent_id = scrapy.Field()


class RegionItem(scrapy.Item):
    name = scrapy.Field()    # 地区名
    id = scrapy.Field()     # id
    parent_id = scrapy.Field()

class CommentItem(scrapy.Item):
    kouwei = scrapy.Field()  # 口味评分
    huanjing = scrapy.Field()  # 环境评分
    fuwu = scrapy.Field()  # 服务评分
    comment = scrapy.Field()  # 评价内容

    user_id = scrapy.Field()  # 评论者id
    user_name = scrapy.Field()
    user_avator = scrapy.Field()
    imgs_url = scrapy.Field()
