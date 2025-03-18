import json
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
PATH_ARCHIVE = ROOT_FOLDER / 'banco.json'

def find_item(name: str):
    count = 0
    for i in data['items']: 
        current_name: str = i['name']
        current_code = i['code']
        if name.lower() in current_name.lower():
            count += 1
            print(f'({count}) Nome: {current_name} - Código: {current_code}\n')
    if count == 0:
        print('Não há dados no sistema.\n')

with open(PATH_ARCHIVE, 'r', encoding='utf-8') as archive:
    data = json.load(archive)

while True:
    name = input('Nome do item: ')
    find_item(name)
    quit_program = input('Deseja sair do programa? (s/n) ').lower()
    if quit_program == 's':
        break

print('Fechando programa!')