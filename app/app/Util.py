# -*- coding: utf-8 -*-
# @Time    : 2017/11/19 17:30
# @Author  : Hua
# @Site    : 
# @File    : Util.py
# @Software: PyCharm

class SortType(object):
    distance_close = 1
    evaluate_good = 2
    price_low = 3
    price_high = 4

    @classmethod
    def getOrderField(cls, type):
        if type == cls.distance_close:
            return 'ave_score'
        elif type == cls.evaluate_good:
            return 'ave_score DESC'
        elif type == cls.price_low:
            return 'ave_price'
        elif type == cls.price_high:
            return 'ave_price DESC'
