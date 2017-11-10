cd /app
rm -rf dianping
git clone https://github.com/myhearter/dianping.git
cd dianping/app
docker build -t myflask .
docker rm dianping_flask -f
docker run -d --name dianping_flask -p 8000:80 --link=dianping-mysql:db myflask