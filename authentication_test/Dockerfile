FROM ubuntu:18.04 AS BUILD_IMAGE

WORKDIR /app

COPY authentication_test.py /app/authentication_test.py

# Install required Python libraries
RUN pip3 install --no-cache-dir requests

# EXPOSE 8000

# Set the environment variable for logging (optional)
ENV LOG=1

CMD ["python3", "authentication_test.py"] 