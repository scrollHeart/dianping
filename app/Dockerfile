FROM tiangolo/uwsgi-nginx-flask:python2.7

MAINTAINER author <geekerhua@sina.com>

COPY requirements.txt ./
COPY nginx.conf /etc/nginx/conf.d/nginx2.conf
COPY mycert/mycert.cert /etc/nginx/cert/
COPY mycert/mycert.key /etc/nginx/cert/
COPY ./app /app

RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

HEALTHCHECK --interval=5s --timeout=2s --retries=10 \
  CMD curl --silent --fail localhost/inde.html || exit 1
