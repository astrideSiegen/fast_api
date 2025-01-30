FROM python:3.9


ADD authentication_test.py  /app/authentication_test.py 

WORKDIR /app

RUN apt-get update && apt-get install python3-pip -y 
RUN pip install iPython 
RUN pip install requests
RUN pip install os

EXPOSE 8000

# ENV LOG=1
CMD ["iPython ", "authentication_test.py", "--host", "0.0.0.0", "--port", "8000" ] 