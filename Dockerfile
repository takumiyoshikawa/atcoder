FROM ubuntu:20.04
LABEL maintainer="Tokuma Suzuki tokuma.suzuki09@gmail.com"

ENV SHELL /bin/bash
ENV DEBIAN_FRONTEND noninteractive


## C++のビルドなどに必要なものを入れる
RUN apt-get update && apt-get install -y \
    build-essential cmake git wget  && \
    # python install
    apt-get install -y python3.8 python3.8-venv python3-pip && \
    # clean-up
    apt-get autoremove -y && \
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /usr/local/src/*

# Python Libraries
COPY requirements.txt /tmp
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt


CMD ["/bin/bash"]
