"""
List comprehension em Python
List comprehension é uma forma rápida para criar listas a partir de iteráveis.
"""
# print(list(range(10)))

# lista = []
# for numero in range(10):
#     lista.append(numero)
# print(lista)

# list comprehension
lista = [numero for numero in range(10)] 
lista_duplica = [numero * 2 for numero in range(10)] 
print(lista)
print(lista_duplica)
