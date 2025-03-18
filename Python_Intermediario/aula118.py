# filter é um filtro funcional
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def filtrar_preco(produto):
    return produto['preco'] > 15

#  list comprehension
novos_produtos = [
    p for p in produtos
    if p['preco'] > 15
] 

# metodo filter
novos_produtos = filter(
    lambda p: p['preco'] > 15,
    # filtrar_preco,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)

# mais_caro = max(produtos, key=lambda x: x['preco'])
# print(mais_caro)

# print(
#     list(
#         map(
#             lambda x: x % 2 == 0,
#             [1, 2, 3, 4, 5, 6]
#         )
#     )
# )

# soma = lambda x, y: x + y
# soma_resultado = soma(3, 6)

# exponencia = lambda x, y: x ** y
# exponencia_resultado = exponencia(2, 10)

# print(soma_resultado)
# print(exponencia_resultado)