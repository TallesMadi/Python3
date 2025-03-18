# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Talles', 'Raquel', 1, 2, 3, 'Luna']
tupla = 'Python', 'é', 'legal'
listona = [[1, 2, 3], [4], [5, 6, [7]], 8, 9]

# p, *_, u = lista
# print(p, u)

print(*lista) # passa todos os itens da lista em  linha
print(*string)
print(*tupla)
print(*listona, sep='\n')
