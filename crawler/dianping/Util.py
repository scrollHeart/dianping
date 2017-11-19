# -*- coding: utf-8 -*-
# @Time    : 2017/11/19 16:30
# @Author  : Hua
# @Site    : 
# @File    : Util.py
# @Software: PyCharm


def getXpathFirst(extract, default=None):
    if extract:
        return extract[0]
    else:
        return default
