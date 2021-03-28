#!/usr/bin/env bash

echo "starting handle_stock ..."



# 判断是什么操作系统
is_win=0
cwd=`pwd`

if [ "$(uname)" == "Darwin" ]; then
    echo 'mac os'
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    echo "Linux"
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
    is_win=1
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
    is_win=1
    cwd=`pwd -W`
fi


#读取env文件内容
if [ -f ".env" ]; then
  echo "load variable from .env file"
  while read line; do export $line; done < .env
fi


function start_develop_docker_env() {
    
    IS_CONTAINER_EXIST=`docker ps -a --filter name=marmota | wc -l`
    if [ $IS_CONTAINER_EXIST -ge 2 ]; then
      echo "stop & rm stock env ..."
      docker stop marmota && docker rm marmota
    fi
    echo "启动开发者模式的docker环境"
    docker run -itd --name marmota \
      -e LANG=zh_CN.UTF-8 -e LC_CTYPE=zh_CN.UTF-8 -e PYTHONIOENCODING=utf-8 \
      -p 5000:5000  --restart=always \
      -v $cwd/web:/data/workspace/web \
      -v $cwd/marmota:/data/workspace/marmota \
      -v $cwd/supervisor:/data/workspace/supervisor \
      hxshandle/ffmpeg-python3.8:latest
    echo "启动完成"
}


demo() {
  IS_CONTAINER_EXIST=`docker ps --filter name=marmota | wc -l`
  if [ $IS_CONTAINER_EXIST -ge 2 ]; then
    echo "stop & rm stock ..."
    docker stop marmota && docker rm marmota
  fi
  echo "in demo $abc"
}

function start_online_docker_env() {
    echo "启动在线模式的docker环境"
}



## 不带参数默认使用开发者模式
if [ $# == 1 ] ; then
  start_online_docker_env
  exit 1;
else
  start_develop_docker_env
  # demo
  exit 1;
fi