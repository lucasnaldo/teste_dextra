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
print('PROCESSO INICIADO')

dm = dextra_manager()
dm.processo()

# FINALIZANDO TEMPO EXECUÇÃO
print('PROCESSO FINALIZADO')
tempo_fim = datetime.datetime.utcnow()
print("Tempo de execução: ", tempo_fim - tempo_exec)