"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

def soma(*args):
    soma = 0
    for numero in args:
        soma += numero
    return soma

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(soma(*numeros))

print(soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
