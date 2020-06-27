from dextra import dextra_manager
import time
import os
import datetime
import sys
from datetime import date, timedelta
import argparse

# INICIANDO TEMPO EXECUÇÃO
tempo_exec = datetime.datetime.utcnow()
print(tempo_exec)
print('INICIOU O PROCESSO')

dm = dextra_manager()
dm.processo()

# FINALIZANDO TEMPO EXECUÇÃO
tempo_fim = datetime.datetime.utcnow()
print(tempo_fim - tempo_exec)

# dextra\quandl_api.py