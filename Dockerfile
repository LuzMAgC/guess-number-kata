FROM python:latest

RUN pip install coverage
RUN pip install pytest-cov
RUN pip install unittest_data_provider

WORKDIR /code
VOLUME ["/code"]
