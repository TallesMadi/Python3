# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest

# minha função
# def zipper(lista1, lista2):
#     if len(lista1) > len(lista2):
#         menor_lista = lista2
#     else:
#         menor_lista = lista1
#     lista_completa = []
#     for i in range(0, len(menor_lista)):
#         lista_completa += [(lista1[i], lista2[i])]
#     return lista_completa

# função do professor
def zipper(lista1, lista2):
    indice_maximo = min(len(lista1), len(lista2))
    return [
        (lista1[i], lista2[i]) for i in range(indice_maximo)
    ]

cidades =  ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

print(zipper(cidades, estados))
print(list(zip(cidades, estados)))
print(list(zip_longest(cidades, estados, fillvalue=('Sem Valor'))))
