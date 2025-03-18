"""
Listas em python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, etc
"""

string = 'ABCDE' # 5 caracteres (len)

lista = [1, True, 'Talles', 1.7, []] #list()

lista[-3] = 'Madi'

for i in range(0, len(lista)):
    print(lista[i], type(lista[i]))
    