FROM ubuntu:18.04 AS BUILD_IMAGE

WORKDIR /app

COPY authorization_test.py /app/authorization_test.py

RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip3 install --no-cache-dir requests

ENV LOG=1

CMD ["python3", "authorization_test.py"] 