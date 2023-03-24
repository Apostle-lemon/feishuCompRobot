FROM python:slim-bullseye

WORKDIR /spider

COPY ./deployments/requirements.txt ./  

RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN pip config set install.trusted-host mirrors.aliyun.com
RUN pip install -U pip

RUN pip install --no-cache-dir -r requirements.txt

COPY ./python /spider