"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40, 50]
lista[0] = 7
# del(lista) apaga a lista
del(lista[1]) # apaga um índice
valor_removido = lista.pop() # apaga o ultimo item da lista
print(valor_removido)
lista.append(60) # adiciona no fim da lista

print(lista)