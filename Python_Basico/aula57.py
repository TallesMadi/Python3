"""
enumerate  = enumera iteráveis (índices)
"""
lista = ['Talles', 'Raquel', 'Luna']
#print(next(lista_enumerada))

# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)

# for indice, nome in enumerate(lista):
#     print(f'Índice: {indice}, Nome: {nome}')

for tupla_enumerada in enumerate(lista):
    print('for da tupla')
    for valor in tupla_enumerada:
        print(f'\t{valor}')