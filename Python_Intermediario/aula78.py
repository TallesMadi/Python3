# manipulando chaves e valores em dicionários
pessoa = {}

chave = 'Nome'

pessoa[chave] = 'Milisandre'
pessoa['Sobrenome'] = 'Marcondez' 
lista = []

print(pessoa)
del pessoa['Sobrenome']
print(pessoa)

if pessoa.get('Sobrenome'): # retorna None se chave não existir
    print(pessoa['Sobrenome'])
else:
    print('Não existe')
