FROM ubuntu:bionic
FROM python:3.7

RUN apt-get update && apt-get -y install cmake
RUN pip install ninja
RUN git clone https://github.com/HighCWu/cheerp-meta
RUN cd cheerp-meta && sh build.sh
