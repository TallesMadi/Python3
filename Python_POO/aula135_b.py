import json

CAMINHO_ARQUIVO = 'C:\\Python3\\Python_POO\\aula135.json'

with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)