FROM ubuntu:20.04

RUN sed -i s:/archive.ubuntu.com:/mirrors.tuna.tsinghua.edu.cn/ubuntu:g /etc/apt/sources.list
RUN cat /etc/apt/sources.list

RUN apt-get update -y && \
    apt-get install -y python3-pip python3.8-dev 
    #apt install -y libmysqlclient-dev
#RUN apt install pkg-config 