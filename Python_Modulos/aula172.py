# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
date_start = datetime.strptime('13/11/1987 23:06:14', fmt)
date_end = datetime.strptime('27/01/2025 13:53:33', fmt)

delta = date_end - date_start
delta2 = timedelta(days=10)
# print(date_end + delta2)

print(date_end)
print(date_end + relativedelta(days=100, hours=10, minutes=6, seconds=27))

# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())

# print(date_start > date_end)
# print(date_start < date_end)
# print(date_start == date_end)