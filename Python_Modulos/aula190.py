# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
import locale, string
from datetime import datetime
from pathlib import Path

locale.setlocale(locale.LC_ALL, '')
PATH_ARCHIVE = Path(__file__).parent / r'aula190.txt'

def convert_brl(number: float) -> str:
    brl = 'R$' + locale.currency(val=number, symbol=False, grouping=True)
    return brl

date = datetime(2025, 1, 30)
data = dict(
    name ='Talles',
    value = convert_brl(1_234),
    date = date.strftime('%d/%m/%Y'),
    enterprise = 'O.M',
    phone = '+55 (17) 99166-6666'
)
# print(data)

class MyTemplate(string.Template):
    delimiter = '%'

with open(PATH_ARCHIVE, 'r', encoding='utf-8') as archive:
    text = archive.read()
    template = MyTemplate(text)
    print(template.substitute(data))

