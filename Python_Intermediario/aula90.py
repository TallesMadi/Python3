# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Preta',
    'preco': 2.5,
    'categoria': 'Escritório'
}

dictionary_comprehension = {
    chave: valor 
    if isinstance(valor, (float, int)) else valor.upper()
    for chave, valor in produto.items()
    if chave != 'categoria'
}

print(dictionary_comprehension)

set_comprehension = {2 ** i for i in range(10)}
print(set_comprehension)