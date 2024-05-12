set -xe

PORT=4396 # 映射端口，宿主机的某个端口映射到容器的80端口
DIR=$(cd $(dirname \$0) && pwd) # 当前脚本所在目录, 将当前目录挂载到容器的/api目录下，更新当前目录代码时，容器中的代码也会更新，不用重新构建镜像
WORKER_NUM=2 # 通过环境变量来设置gunicorn的进程数，默认为1

docker run -d --name flask-api -p $PORT:80 -v $DIR:/api -e WORKER_NUM=$WORKER_NUM --restart=always flask-api
