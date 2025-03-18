"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa - iterável + tamanho de grupo
Permutação - Ordem importa
Produto - Ordem importe e repete valores únicos
"""
from itertools import combinations, permutations, product

def print_iter(iterador):
    print(*list(iterador), sep='\n')


pessoas = ['Talles', 'Raquel', 'Luna', 'Maria Flor']

camisetas = [
    ['Preta', 'Branca'],
    ['Seda', 'Algodão'],
    ['P', 'M', 'G'],
    ['Masculino', 'Femino']
]

print_iter(combinations(pessoas, 2)) # lista, grupo de x valores
print('-'*40)
print_iter(permutations(pessoas, 2))
print('-'*40)
print_iter(product(*camisetas))