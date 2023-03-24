FROM python:3.10

WORKDIR /spider

COPY ./deployments/requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt

COPY . /spider