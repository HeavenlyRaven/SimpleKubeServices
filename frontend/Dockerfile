FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY frontend.py frontend.py 

ENV IP="0.0.0.0"

EXPOSE 80

ENTRYPOINT gunicorn -b ${IP}:80 frontend:app