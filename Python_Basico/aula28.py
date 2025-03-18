"""
introdução ao try/except
try -> tentar executar o código
except -> ocorreu um erro ao tentar executar
"""
# ao pressionar F2 em cima de uma variável X, você pode mudar o nome de todas as variaveis X.
numero_str = input('Digite um número para eu te mostrar o dobro dele: ')

# print(numero_str.isdigit()) só aceita numeros
try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_float} é {numero_float * 2}')
except:
    print(f'"{numero_str}" não é um número!')




