import json

caminho = 'C:\\Python3\\Python_Intermediario\\aula123.json'

# pessoa = {
#     'nome': 'Talles',
#     'sobrenome': 'Madi',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.93,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# with open(caminho, 'w', encoding='utf-8') as arquivo:
#     json.dump(
#         pessoa,
#         arquivo,
#         ensure_ascii=False,
#         indent=2
#     )

with open(caminho, 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])