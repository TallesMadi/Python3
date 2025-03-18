# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta

date_start = datetime.strptime('20/12/2020', '%d/%m/%Y')
date_end = date_start + relativedelta(years=5)

parcelas = 0
while date_start != date_end:
    print(date_start)
    parcelas += 1
    date_start += relativedelta(months=1)
print(date_start)

print(f'Você pegou um total de R$1.000.000 para pagar em 5 anos')
print(f'Foram {parcelas} parcelas de R${(1000000 / parcelas):.2f} cada!')