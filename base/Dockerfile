FROM ubuntu:18.04 AS BUILD_IMAGE

WORKDIR /app

RUN mkdir /app/logs

# Install required Python libraries
RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip3 install --no-cache-dir requests