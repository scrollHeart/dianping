FROM python:2

MAINTAINER GeekerHua <geekerhua@sina.com>

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

COPY . .
WORKDIR /usr/src/app/dianping

#CMD [ "scrapy", "crawl", "merchants" ]
