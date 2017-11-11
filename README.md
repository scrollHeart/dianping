点评网的爬虫

服务器留一个hock的服务，当git push的时候，就进行dockerbuild。重启服务。


# docker 的部署备忘
## flask
docker build -t myflask .
docker run -d --name dianping_flask -p 80:80 --link=dianping_mysql:db myflask

## mysql
docker run -d --name dianping_mysql -e MYSQL_ROOT_PASSWORD=1234qwer -p 3306:3306 mysql

## scrapy
docker build -t my-python-app .
docker run -it --name dianping_scrapy --link=dianping_mysql:db my-python-app


docker run -it --rm --name my-running-app --link my-python-app

docker run -it --name dianping_scrapy --link=dianping-mysql:db my-python-app /usr/bin/mysql -h db -u root -p1234qwer

## 原型图
(https://modao.cc/app/LP9kj7CNqD7jgsvJX7KHLC5tIP7HSbj#screen=s8EF112C74B1508314956150)[https://modao.cc/app/LP9kj7CNqD7jgsvJX7KHLC5tIP7HSbj#screen=s8EF112C74B1508314956150]

create database dianping charset=utf8;

create table T_merchants(id int auto_increment primary key, comment varchar(20) NULL, name varchar(30) NULL, huanjing double default '0' NUll, fuwu double default '0' NULL, kouwei double default '0' NULL, tag varchar(20) NULL);