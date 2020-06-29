import requests
import os
import json
import pandas as pd
import numpy as np
import sqlite3
from sympy import *
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
        dir_path = os.path.dirname(os.path.realpath(__file__))
        df = pd.read_csv(dir_path+'/Ativos.csv', delimiter = ';')

        ### Remove Unknow columns
        df = df.drop(df.columns[[3,4,5]], axis=1)

        ### Cria coluna com data atual
        df.insert(loc=2, column='data_atual', value=datetime)
        df['data_atual'] = data_atual

        ### Force Datetime to 'vencimento' field
        df['data_atual'] = df['data_atual'].apply(pd.to_datetime)
        df['vencimento'] = df['vencimento'].apply(pd.to_datetime)

        ### Calcula diferença de meses a partir da data atual em nova coluna
        df['anos_diff'] = ((df['vencimento'] - df['data_atual'])/np.timedelta64(1, 'Y')).astype(int)

        ### Cria colunas preco_fix e selic
        df.insert(loc=2, column='preco_fix', value=float)

        ### Replace object money type (str) to float type
        df['preco_fix'] = df['preco'].str.replace('49510,47', 'R$ 49510,47')
        df['preco_fix'] = df['preco_fix'].str.replace('.', '')
        df['preco_fix'] = df['preco_fix'].str.replace(',', '.')
        df['preco_fix'] = df['preco_fix'].str[3:]
        df['preco_fix'] = df['preco_fix'].astype(float)

        ### Sort by Datetime
        df = df.sort_values(by=['vencimento'])
        df.loc['a']=['inicial', '-R$300.000,00', -300000, data_atual, data_atual, 0]
        newIndex=['a']+[ind for ind in df.index if ind!='a']
        df=df.reindex(index=newIndex)

        cash_flow = df['preco_fix'].values 
        irr = round(((np.irr(df['preco_fix']))*100),1)
        print("A TIR para esse fluxo de caixa é de: {}% \nenquanto a selic atual é de:{}%".format(irr, selic))

        ### Force Datetime to 'vencimento' field
        df['data_atual'] = df['data_atual'].apply(pd.to_datetime)
        df['vencimento'] = df['vencimento'].apply(pd.to_datetime)

        ### Cria conexão sql na memoria
        conn = sqlite3.connect(':memory:',detect_types=sqlite3.PARSE_DECLTYPES,uri=True)

        ### Converte DataFrame para formato SQL, cria a tabela e salva os dados
        df.to_sql(name='ativ', con=conn)

        ### Select da nova tabela para testar os valores
        sql_tudo = pd.read_sql('select * from ativ', conn)
        print("\nESSA TABELA É DE UMA CONSULTA SQL IN MEMORY\n")
        print(sql_tudo)

