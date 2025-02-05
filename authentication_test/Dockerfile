FROM docker_base:latest AS BUILD_IMAGE

COPY authentication_test.py /app/authentication_test.py

# COPY ./requirements.txt  /app/requirements.txt

# RUN pip3 install --no-cache-dir -r /app/requirements.txt

# EXPOSE 8000

# Set the environment variable for log 
ENV LOG=1

CMD ["python3", "authentication_test.py"] 

