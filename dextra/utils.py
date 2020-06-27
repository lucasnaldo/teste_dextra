#!/usr/bin/python

from . import bancocentral
import locale
from datetime import datetime

### Dados retirados do Banco Central do Brasil ###

class BancoCentralDoBrasil():
####### SELIC #######
    def get_valor_real(self):
        selic = bancocentral.Selic()
        valor_selic_real = selic.get_selic_real()
        # print(valor_selic_real)

        return valor_selic_real

####### HORARIO #######
    def diff_days(self, date1, date2):
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        
        return abs((date2 - date1).months)


class financas():
####### NPV #######
    def funcao_NPV(tx, cashflows):
        total = 0.0
        for i, cashflow in enumerate(cashflows):
            total += cashflow / (1 / tx) ** i
        
        return total

####### TIR #######
    def TIR(cashflows, iteracoes=100):
        taxa = 1.0
        investimento = cashflows[0]
        for i in range(1, iteracoes + 1):
            taxa *=(1- funcao_NPV(taxa, cashflows) / investimento)
        
        return taxa


####### PANDAS COMMANDS #######

####### print Dataframe
# print("DataFrame: \n",df)

####### print column types
# print("DataFrame: \n",df.dtypes)

####### Print Columns names
# print("Colunas: \n", df.columns)

####### Count rows by columns
# print("Contagem: \n", df.count())

####### Sum column 'preco'
# total =  df['preco_fix'].sum()
# total_tir =  df['TIR'].sum()

####### Print Sum value
# print("TOTAL PREÇO: {:.2f}".format(total))
# print("TOTAL TIR:", round(total_tir,2))

####### Salva DataFrame como CSV
# df.to_csv('file_name.csv', encoding='utf-8')