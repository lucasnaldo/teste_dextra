import requests
import json
import pandas as pd
import numpy as np
import sqlite3
# from . import utils
from .utils import BancoCentralDoBrasil, financas
from datetime import datetime
from datetime import date


class dextra_manager():

    def processo(self):
        ### Data Atual
        data_atual = date.today()

        ### Get Selic value
        bc = BancoCentralDoBrasil()
        selic = bc.get_valor_real()

        ### Read CSV File
        df = pd.read_csv('dextra\Ativos.csv', delimiter = ';')

        ### Remove Unknow columns
        df = df.drop(df.columns[[3,4,5]], axis=1)

        ### Cria coluna com data atual
        df.insert(loc=2, column='data_atual', value=datetime)
        df['data_atual'] = data_atual

        ### Force Datetime to 'vencimento' field
        df['data_atual'] = df['data_atual'].apply(pd.to_datetime)
        df['vencimento'] = df['vencimento'].apply(pd.to_datetime)

        ### Calcula diferença de meses a partir da data atual em nova coluna
        df['data_diff'] = ((df['vencimento'] - df['data_atual'])/np.timedelta64(1, 'M')).astype(int)

        ### Cria colunas preco_fix e selic
        df.insert(loc=2, column='preco_fix', value=float)
        df.insert(loc=3, column='selic', value=selic)

        ### Replace object money type (str) to float type
        df['preco_fix'] = df['preco'].str.replace('49510,47', 'R$ 49510,47')
        df['preco_fix'] = df['preco_fix'].str.replace('.', '')
        df['preco_fix'] = df['preco_fix'].str.replace(',', '.')
        df['preco_fix'] = df['preco_fix'].str[3:]
        df['preco_fix'] = df['preco_fix'].astype(float)


        ### Calcula porcentagem entre valor inicial (R$300.000,00 e preço)
        df['TIR'] = round((df['preco_fix'] / 300000 * 100),2)

        ### Sort by Datetime
        df = df.sort_values(by=['vencimento'])

        ### Cria conexão sql na memoria
        conn = sqlite3.connect(':memory:',detect_types=sqlite3.PARSE_DECLTYPES,uri=True)

        ### Converte DataFrame para formato SQL, cria a tabela e salva os dados
        df.to_sql(name='ativ', con=conn)

        ### Select da nova tabela para testar os valores
        sql_tudo = pd.read_sql('select * from ativ', conn)
        sql_preco = pd.read_sql('select preco from ativ', conn)
        print(sql_tudo)
        print(sql_preco)

