# -*- coding: utf-8 -*-
# @Time    : 2017/10/11 11:03
# @Author  : Hua
# @Site    :
# @File    : app.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
import commands
from flask import Flask

app = Flask(__name__)
ip = '172.19.101.220'

@app.route("/hook", methods='POST')
def hook():
    # cmd = "cd /home/hua/dianping/app && git pull && docker build -t myflask . && docker rm dianping_flask -f && docker run -d --name dianping_flask -p 8000:80 --link=dianping-mysql:db myflask"
    cmd = 'ssh hua@{} "bash run.sh"'.format(ip)

    result = commands.getoutput(cmd)
    return result, 'success'


@app.route("/")
def hello():
    return "Dear honey"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
