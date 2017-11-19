# -*- coding: utf-8 -*-
# @Time    : 2017/10/11 11:03
# @Author  : Hua
# @Site    : 
# @File    : app.py.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
import os

import MySQLdb
import MySQLdb.cursors
from flask import Flask, Response, jsonify, request
from flasgger import Swagger
from Util import SortType


app = Flask(__name__)
Swagger(app)
# app.config['SECRET_KEY'] = 'Fianna'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234qwer@localhost:3306/dianping'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db = SQLAlchemy(app)
DB_ADDR = os.getenv('DB_PORT_3306_TCP_ADDR', 'localhost')
DB_PORT = int(os.getenv('DB_PORT_3306_TCP_PORT', 3306))
DB_PASSWORD = os.getenv('DB_ENV_MYSQL_ROOT_PASSWORD', '********')


def getList(count=20, page=1, keywords=None, sort=2):
    coon = MySQLdb.connect(host=DB_ADDR, port=DB_PORT, user='root', passwd=DB_PASSWORD, db='dianping', charset='utf8',
                           cursorclass=MySQLdb.cursors.DictCursor)
    cursor = coon.cursor()
    page -= 1
    search_sql = 'WHERE name LIKE "%{keywords}%"'.format(keywords=keywords) if keywords else ''
    sql = 'select T_merchants.id, T_merchants.name, T_merchants.ave_price, T_merchants.comment_count, T_merchants.img_url, T_merchants.star, T_merchants.tag, T_classfy.name as classfy_name, T_region.name as region_name,round((kouwei+fuwu+huanjing)/3,1) as ave_score FROM T_merchants LEFT JOIN T_classfy ON T_merchants.classfy=T_classfy.id LEFT JOIN T_region ON T_merchants.region=T_region.id {search_sql} ORDER BY {order_by} LIMIT {offset},{count}'.format(
        count=count, offset=page * count, keywords=keywords, order_by=SortType.getOrderField(sort),
        search_sql=search_sql)
    print sql
    cursor.execute(sql)
    result = cursor.fetchall()
    coon.close()
    return result


def shopDetail(shop_id):
    coon = MySQLdb.connect(host=DB_ADDR, port=DB_PORT, user='root', passwd=DB_PASSWORD, db='dianping', charset='utf8',
                           cursorclass=MySQLdb.cursors.DictCursor)
    cursor = coon.cursor()
    search_sql = 'WHERE T_merchants.id="{shop_id}"'.format(shop_id=shop_id)
    sql = 'select T_merchants.*, T_classfy.name as classfy_name, T_region.name as region_name FROM T_merchants LEFT JOIN T_classfy ON T_merchants.classfy=T_classfy.id LEFT JOIN T_region ON T_merchants.region=T_region.id {search_sql}'.format(
        search_sql=search_sql)
    # sql = 'select T_merchants.id, T_merchants.name, T_merchants.ave_price, T_merchants.comment_count, T_merchants.img_url, T_merchants.star, T_merchants.tag, T_classfy.name as classfy_name, T_region.name as region_name,round((kouwei+fuwu+huanjing)/3,1) as ave_score FROM T_merchants LEFT JOIN T_classfy ON T_merchants.classfy=T_classfy.id LEFT JOIN T_region ON T_merchants.region=T_region.id {search_sql}'.format(search_sql=search_sql)
    print sql
    cursor.execute(sql)
    result = cursor.fetchone()
    coon.close()
    return result


@app.route("/")
def hello():
    return "Dear honey"


@app.route('/shops/recommend')
def recommend():
    """
        猜你喜欢
        暂时推荐高分商户
        ---
        tags:
          - merchants
        parameters:
          - name: page
            in: query
            type: integer
            description: 页码，从1开始
          - name: count
            in: query
            type: int
            description: 每页显示条数，默认20
        responses:
          200:
            description: 请求成功数据结构
            schema:
              type: array
              items:
                properties:
                  name:
                    type: string
                    description: 商户名称
                    default: KFC
                  id:
                    type: int
                    description: id
                    default: 1
                  star:
                    type: string
                    description: 商户等级
                    default: 五星商户
                  fuwu:
                    type: float
                    description: 服务评分
                    default: 9
                  huanjing:
                    type: float
                    description: 环境评分
                    default: 8.5
                  kouwei:
                    type: float
                    description: 口味评分
                    default: 8.0
                  tag:
                    type: string
                    description: tag
                    default: 商户分类

            """
    page = request.args.get('page', 1)
    count = request.args.get('count', 20)
    page = int(page) if page else 1
    count = int(count) if count else 20
    return jsonify(getList(count=count, page=page, sort=2))


@app.route('/shops')
def searchShop():
    """
        搜索商户信息
        根据商户名进行搜索，能够进行排序
        ---
        tags:
          - merchants
        parameters:
          - name: keywords
            in: query
            type: string
            description: 页码，从1开始
          - name: page
            in: query
            type: integer
            description: 页码，从1开始
          - name: count
            in: query
            type: int
            description: 每页显示条数，默认20
          - name: sort
            in: query
            type: int
            description: 排序方式。1：离我最近，2：评价最好， 3：人均最低，4：人均最高。默认值2
        responses:
          200:
            description: 请求成功数据结构
            schema:
              type: array
              items:
                properties:
                  name:
                    type: string
                    description: 商户名称
                    default: KFC
                  id:
                    type: int
                    description: id
                    default: 1
                  star:
                    type: string
                    description: 商户等级
                    default: 五星商户
                  fuwu:
                    type: float
                    description: 服务评分
                    default: 9
                  huanjing:
                    type: float
                    description: 环境评分
                    default: 8.5
                  kouwei:
                    type: float
                    description: 口味评分
                    default: 8.0
                  tag:
                    type: string
                    description: tag
                    default: 商户分类

        """
    keywords = request.args.get('keywords')
    keywords = keywords.encode('utf-8') if keywords else None
    page = request.args.get('page')
    count = request.args.get('count')
    sort = request.args.get('sort')
    page = int(page) if page else 1
    count = int(count) if count else 20
    sort = int(sort) if sort else 4
    return jsonify(getList(keywords=keywords, count=count, page=page, sort=sort))


@app.route('/shop/<int:id>')
def shop(id):
    """
        获取制定商户的详情
        获取制定商户的详细资料，包括评论
        ---
        tags:
          - merchants
        parameters:
          - name: id
            in: path
            type: int
            description: 商户的id
        responses:
          200:
            description: 请求成功数据结构
            schema:
              type: array
              items:
                properties:
                  name:
                    type: string
                    description: 商户名称
                    default: KFC
                  id:
                    type: int
                    description: id
                    default: 1
                  star:
                    type: string
                    description: 商户等级
                    default: 五星商户
                  fuwu:
                    type: float
                    description: 服务评分
                    default: 9
                  huanjing:
                    type: float
                    description: 环境评分
                    default: 8.5
                  kouwei:
                    type: float
                    description: 口味评分
                    default: 8.0
                  tag:
                    type: string
                    description: tag
                    default: 商户分类

        """
    return jsonify(shopDetail(id))


if __name__ == '__main__':
    if DB_ADDR == 'localhost':
        app.run(host='0.0.0.0', debug=True, port=8000)
    else:
        app.run(host='0.0.0.0', debug=True, port=80, ssl_context=(
            '/etc/nginx/cert/mycert.cer', '/etc/nginx/cert/mycert.key'))
