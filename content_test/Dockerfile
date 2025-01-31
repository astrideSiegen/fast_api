FROM ubuntu:18.04

WORKDIR /app

COPY content_test.py /app/content_test.py

RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip3 install --no-cache-dir requests

ENV LOG=1

CMD ["python3", "content_test.py"] 