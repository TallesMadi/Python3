# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
# venv\Scripts\activate - ativar ambiente virtual

from datetime import datetime
from pytz import timezone

data_str_data = '27/01/2025 13:31:56'
data_str_format = '%d/%m/%Y %H:%M:%S'

print(datetime(2025, 1, 27))
print(datetime(2025, 1, 27, 13, 26))
print(datetime.strptime(data_str_data, data_str_format))
print('-'*20)

print(datetime(2025, 1, 27, 13, 26, tzinfo=timezone('Asia/Tokyo')))
print(datetime.now(timezone('America/Sao_Paulo')))
print(datetime.now(timezone('Asia/Tokyo')))

# numero e segundos de 1/1/1970 até hoje
print(datetime.now().timestamp())

print(datetime.fromtimestamp(1737996623.683017))