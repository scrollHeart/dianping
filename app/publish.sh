#!/usr/bin/env bash

docker build -t myflask .
docker run -d --name dianping_flask -p 80:80 --link=dianping_mysql:db myflask
