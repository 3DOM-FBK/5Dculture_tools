FROM python:3.7

RUN apt update
RUN pip install numpy==1.19.5
# RUN pip install numba llvmlite
RUN pip install paddlepaddle==2.1.1
RUN pip install ppgan
RUN pip install pyeuropeana
RUN pip install wget
RUN pip install protobuf==3.20.1
RUN pip install paddlepaddle==2.4.0rc0

RUN apt-get update && apt-get -y install libgl1

WORKDIR /usr/src/scripts

COPY ./*.py .

ENTRYPOINT [ "python", "main.py" ]
