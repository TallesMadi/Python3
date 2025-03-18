"""
Crie uma função que multiplica todos os argumentos  não nomeados recebidos.
Retrone o total para uma variável e mostra o valor dela

crie uma função que fala se um número é par ou impar
"""

def multiplicar(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

def par_ou_impar(num):
    resultado = 'Par' if num % 2 == 0 else 'Ímpar'
    return resultado

print(multiplicar(7, 7))
print(par_ou_impar(7))