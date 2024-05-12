set -xe

# 切换到当前脚本所在目录
DIR=$(cd $(dirname $0) && pwd)
cd $DIR

echo now start building image...
# 当前脚本所在目录作为构建镜像的上下文
docker build -t flask-api -f Dockerfile $DIR
