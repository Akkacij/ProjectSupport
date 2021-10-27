FROM python:3.7-alpine
ENV PYTHONBUFFERED 1
WORKDIR /ProjectSupport
COPY requirments.txt /ProjectSupport
RUN pip install -r /requirments.txt
COPY . /ProjectSupport/
