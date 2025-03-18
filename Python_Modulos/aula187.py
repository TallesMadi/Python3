# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

PATH_CSV = Path(__file__).parent / 'aula187.csv'

customer_list = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

with open(PATH_CSV, 'w', encoding='utf-8') as archive:
    column_name = customer_list[0].keys()
    writer = csv.DictWriter(archive, fieldnames=column_name)

    writer.writeheader()

    for costumer in customer_list:
        writer.writerow(costumer)

# with open(PATH_CSV, 'w', encoding='utf-8') as archive:
#     column_name = customer_list[0].keys()
#     writer = csv.writer(archive)

#     writer.writerow(column_name)

#     for costumer in customer_list:
#         writer.writerow(costumer.values())