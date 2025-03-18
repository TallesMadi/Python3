# empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Raquel',
    'sobrenome': 'Manzato'
}

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

for chave, valor in pessoa.items():
    print(chave, valor)

dados_pessoa =  {
    'idade': 22,
    'altura': 1.58
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

# args e kwargs
# args argumentos não nomeados
# kwargs  keywords arguments (argumentos nomeados) 

def mostrar_argumentos_nomeados(**kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

# mostrar_argumentos_nomeados(nome='Talles', anos=12)
mostrar_argumentos_nomeados(**pessoa_completa)