FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
ENV PIP_ROOT_USER_ACTION=ignore
WORKDIR /django 
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

