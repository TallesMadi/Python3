# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

PATH_CSV = Path(__file__).parent / 'aula186.csv'

with open(PATH_CSV, 'r', encoding='utf-8') as archive:
    leitor = csv.DictReader(archive)

    for linha in leitor:
        print(linha)

# with open(PATH_CSV, 'r', encoding='utf-8') as archive:
#     leitor = csv.reader(archive)

#     for linha in leitor:
#         print(linha)