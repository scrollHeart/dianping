#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# 2017-09-19 15:39:29
"""

__author__ = 'geekerhua@sina.com'

from django.db import models


class MerchantItem(models.Model):
    star = models.CharField(max_length=20, default=None)
    name = models.CharField(max_length=30, default=None)
    huanjing = models.FloatField(default=0)
    fuwu = models.FloatField(default=0)
    kouwei = models.FloatField(default=0)
    tag = models.CharField(max_length=20, default=None)

    ave_price = models.FloatField(max_length=10, default=None)  # 平均价格
    comment_count = models.IntegerField(default=0)  # 评论数
    phone = models.CharField(max_length=30, default=None, null=True)  # 电话
    address = models.CharField(max_length=60, default=None, null=True)  # 地址
    img_url = models.CharField(max_length=500, default=None, null=True)  # 题图
    detail_url = models.CharField(max_length=100, default=None)  # 详情链接
    id = models.IntegerField(primary_key=True)
    # address tag 格式还需要研究

    city = models.CharField(max_length=10, default=None)
    region = models.CharField(max_length=10, default=None)
    classfy = models.CharField(max_length=10, default=None)

    # classfy = models.ForeignKey('Classfy', to_field='id')
    objects = models.Manager()

    def __str__(self):
        return {'sd': 'ddd'}

    class Meta:
        db_table = 'T_merchants'


class ClassfyItem(models.Model):
    name = models.CharField(max_length=20)
    id = models.CharField(max_length=10, primary_key=True)
    parent_id = models.CharField(max_length=10, default=None, null=True)

    objects = models.Manager()

    class Meta:
        db_table = 'T_classfy'


class RegionItem(models.Model):
    name = models.CharField(max_length=20)
    id = models.CharField(max_length=10, primary_key=True)
    parent_id = models.CharField(max_length=10, default=None, null=True)
    objects = models.Manager()

    class Meta:
        db_table = 'T_region'

