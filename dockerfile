FROM python:3.8-slim
COPY requirements.txt requirements.txt
COPY environments.json /usr/app/environments.json
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt