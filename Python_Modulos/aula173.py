# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

fmt = '%d/%m/%Y'
date = datetime.strptime('2025-01-27 14:26:13', '%Y-%m-%d %H:%M:%S')
print(date)
print(date.strftime(fmt))
print(date.strftime('%Y'))
print(date.strftime('%Y/%m'))