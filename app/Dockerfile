FROM tiangolo/uwsgi-nginx-flask:python2.7

MAINTAINER author <geekerhua@sina.com>

COPY requirements.txt ./
COPY nginx.conf /etc/nginx/conf.d/
COPY mycert/mycert.pem /etc/ssl/
COPY mycert/mycert.key /etc/ssl/

RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

COPY ./app /app