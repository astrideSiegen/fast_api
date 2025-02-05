FROM docker_base:latest AS BUILD_IMAGE

COPY authorization_test.py /app/authorization_test.py

ENV LOG=1

CMD ["python3", "authorization_test.py"] 