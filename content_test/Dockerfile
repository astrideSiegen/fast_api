FROM docker_base:latest as BUILD_IMAGE

COPY content_test.py /app/content_test.py

ENV LOG=1

CMD ["python3", "content_test.py"] 