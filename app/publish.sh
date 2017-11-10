#!/usr/bin/env bash

docker build -t myflask .
docker run -d --name dianping_flask -p 80:80 --link=dianping_mysql:db myflask

sudo docker build -t reg.docker.alibaba-inc.com/yousang/price_inspector:v1.0 ./docker/
sudo docker push reg.docker.alibaba-inc.com/yousang/price_inspector:v1.0