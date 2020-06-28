FROM python:3.7.8

RUN mkdir /teste_dextra

WORKDIR /teste_dextra

COPY requirements.txt requirements.txt

RUN pip uninstall teste_dextra
RUN pip install -r requirements.txt

RUN rm requirements.txt

COPY . .

RUN python setup.py install

CMD ["python", "teste_dextra/app.py"]
