# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
import pprint

def p(valor):
    pprint.pprint(novos_produtos, sort_dicts=False, width=40)

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
# print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

# novos_produtos = [{'nome': produto['nome'], 'preco': produto['preco']} for produto in produtos]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto} 
    for produto in produtos
]

# print(novos_produtos)
# print(*novos_produtos, sep='\n')
# p(novos_produtos)

# filtro de dados em list comprehension (filter)
# lista = [
#     numero for numero in range(10)
#     if numero < 4
# ]
# print(lista)

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto} 
    for produto in produtos
    if produto['preco'] * 1.05 > 10 and produto['preco'] >= 20
]

print(novos_produtos)

# o que vem na esquerda do for em List comprehension é mapeamento,  que vem na direita é filtro
