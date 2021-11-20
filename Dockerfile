FROM ubuntu:20.04

RUN apt update && apt -y upgrade && apt -y install python3 python3-pip
RUN python3 -m pip install pytube