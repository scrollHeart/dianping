FROM tiangolo/uwsgi-nginx-flask:python2.7

MAINTAINER author <geekerhua@sina.com>

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

COPY ./app /app