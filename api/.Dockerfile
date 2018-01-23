FROM python:3.6.3
MAINTAINER ZENSORIUM THAILAND <adisak.s@zensorium.com> 19/01/2018
ADD . /MI
WORKDIR /MI
RUN pip install -r requirements.txt
