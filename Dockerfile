FROM jrottenberg/ffmpeg:4.0-ubuntu2004

WORKDIR     /data/workspace

# set up python 
ENV PATH /usr/local/bin:$PATH

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 替换阿里云的源

RUN echo "deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse\n\
deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse\n\
deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse\n\
deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse\n\
deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse\n\
deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse\n\
deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse\n\
deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse\n\
deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse\n\
deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse\n" > /etc/apt/sources.list

# extra dependencies (over what buildpack-deps already includes)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libbluetooth-dev \
    software-properties-common \
    wget \
    vim \
    curl \
    tk-dev \
    uuid-dev \
  && add-apt-repository ppa:deadsnakes/ppa \
  && apt-get install -y python3.8 python3-pip \
  && rm -rf /var/lib/apt/lists/* \
  && ln -s /usr/bin/python3 /usr/bin/python \
  && ln -s /usr/bin/pip3  /usr/bin/pip


# 设置pip的阿里云代理
RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple \
  && pip config set global.trusted-host mirrors.aliyun.com

# echo  "[global]\n\
# trusted-host=mirrors.aliyun.com\n\
# index-url=http://mirrors.aliyun.com/pypi/simple" > /root/.config/pip/pip.conf && \

ENTRYPOINT  ["/bin/bash"]