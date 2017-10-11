# -*- coding: utf-8 -*-
# @Time    : 2017/10/11 11:03
# @Author  : Hua
# @Site    : 
# @File    : app.py.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
from flask import Flask, Response, jsonify
import MySQLdb
import MySQLdb.cursors
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)
# app.config['SECRET_KEY'] = 'Fianna'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234qwer@localhost:3306/dianping'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db = SQLAlchemy(app)

def getList():
    coon = MySQLdb.connect(host='localhost', user='root', passwd='1234qwer', db='dianping', charset='utf8',
                           cursorclass=MySQLdb.cursors.DictCursor)
    cursor = coon.cursor()
    cursor.execute('select * from T_merchants')
    result = cursor.fetchall()
    coon.close()
    return result


    # parameters:
      # - name: language
      #   in: path
      #   type: string
      #   required: true
      #   description: The language name
      # - name: size
      #   in: query
      #   type: integer
      #   description: size of awesomeness


@app.route('/list', methods=['GET'])
def all():
    """
    show all list
    调用这个方法能够获取到所有商户信息
    ---
    tags:
      - merchants
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
              comment:
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

    return jsonify(getList())


@app.route("/")
def hello():
    return "Dear honey"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
