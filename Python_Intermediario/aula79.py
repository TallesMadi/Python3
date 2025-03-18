# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

pessoa1 = {
    'Nome': 'Talles',
    'Sobrenome': 'Madi',
    'Lista': [0, 1, 2]
}

#copia de listas
pessoa2 = pessoa1.copy() #shallow copy
pessoa3 = copy.deepcopy(pessoa1) #deepcopy
pessoa2['Nome'] = 'Raquel'
pessoa2['Lista'][0] = 7
pessoa3['Nome'] = 'Luna'
pessoa3['Lista'][0] = 66
print(pessoa1)
print(pessoa2)
print(pessoa3)

#métodos de dicionarios
pessoa1.setdefault('Idade', None)
print(pessoa1['Idade'])

print(len(pessoa1))
print(pessoa1.keys())
print(pessoa1.values())
print(pessoa1.items())

for ultima_chave, valor in pessoa1.items():
    print(ultima_chave, valor)

print(pessoa1.get('Nome', 'Não existe'))
nome = pessoa1.pop('Lista')
ultima_chave = pessoa1.popitem()
print(nome)
print(ultima_chave)

pessoa1.update({
    'Nome': 'Cabalos'
})
pessoa1.update(Nome='Selton', Sobrenome='Melo')
print(pessoa1)

