"""
Gerador de CPF
"""
import random

cpf = ''
for i in range(9):
    cpf += str(random.randint(0, 9))

soma_primeiro = 0
for i in range(9):
    soma_primeiro += int(cpf[i]) * (10 - i)
resto_primeiro = soma_primeiro % 11
primeiro_digito = 0 if resto_primeiro < 2 else 11 - resto_primeiro
cpf += str(primeiro_digito)

soma_segundo = 0
for i in range(10):
    soma_segundo += int(cpf[i]) * (11 - i)
resto_segundo = soma_segundo % 11
segundo_digito = 0 if resto_segundo < 2 else 11 - resto_segundo
cpf += str(segundo_digito)
digitos_final = f"{primeiro_digito}{segundo_digito}"
verificacao = cpf[-2:]
if digitos_final == verificacao:
    formatacao = input('Quer o cpf com ou sem formatação? s/n ').lower()
    if formatacao == 's':
        print(f'O seu cpf é: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')   
    else:
         print(f'O seu cpf é: {cpf}')          
