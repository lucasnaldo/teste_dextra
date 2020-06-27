# FROM 295245630435.dkr.ecr.sa-east-1.amazonaws.com/python-docker:latest
# LABEL Author="Lucas Naldo"
# LABEL Version="0.1"
FROM python:3.7.8

RUN apt-get clean && apt-get update && apt-get install -y locales
RUN locale-gen pt_BR.UTF-8

ENV LANG pt_BR.UTF-8
ENV LC_ALL pt_BR.UTF-8

RUN dpkg-reconfigure locales

RUN mkdir /teste_dextra

WORKDIR /teste_dextra

COPY requirements.txt requirements.txt

RUN pip uninstall teste_dextra
RUN pip install -r requirements.txt

RUN rm requirements.txt

COPY . .

RUN python setup.py install

CMD ["python", "teste_dextra/app.py"]
