FROM ubuntu:18.04 AS BUILD_IMAGE

WORKDIR /app

COPY authentication_test.py /app/authentication_test.py

# Install required Python libraries
RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip3 install --no-cache-dir requests

# COPY ./requirements.txt  /app/requirements.txt

# RUN pip3 install --no-cache-dir -r /app/requirements.txt

# EXPOSE 8000

# Set the environment variable for logging (optional)
ENV LOG=1

CMD ["python3", "authentication_test.py"] 

