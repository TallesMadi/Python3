import json
from copy import deepcopy
# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON e depois crie novamente as instâncias da classe com os dados salvos.
# Faça em arquivos separados

CAMINHO_ARQUIVO = 'C:\\Python3\\Python_POO\\aula135.json'

class Pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

p1 = Pessoa('Talles', 'Madi', 20)

dicionario_p1 = deepcopy(vars(p1))

with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(
        dicionario_p1,
        arquivo,
        ensure_ascii=False, 
        indent=2
    )
