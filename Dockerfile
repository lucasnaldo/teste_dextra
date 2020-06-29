FROM python:3.7

# RUN apt-get clean && apt-get update && apt-get install
RUN apt-get update \
 && apt-get install unixodbc -y \
 && apt-get install unixodbc-dev -y \
 && apt-get install freetds-dev -y \
 && apt-get install freetds-bin -y \
 && apt-get install tdsodbc -y \
 && apt-get install --reinstall build-essential -y

RUN mkdir /teste_dextra

WORKDIR /

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN rm requirements.txt

COPY . .

RUN python setup.py install

CMD ["python", "app.py"]
