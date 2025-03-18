"""
Retorno de valores das funções (return)
"""

def par_ou_impar(x):
    resposta = 'Par' if x % 2 == 0 else 'Ímpar'
    return resposta

print(par_ou_impar(7))
print(par_ou_impar(0))
print(par_ou_impar(10))
print(par_ou_impar(8))
print(par_ou_impar(11))