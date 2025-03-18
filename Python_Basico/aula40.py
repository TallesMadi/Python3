"""
Iterando strings com while
"""

nome = 'Talles Madi' #iteráveis
contador = 0
tamanho_nome = len(nome)
nome_asterisco = ''

while contador < tamanho_nome:
    nome_asterisco += f'*{nome[contador]}'
    contador += 1
nome_asterisco += '*'
print(nome_asterisco)
