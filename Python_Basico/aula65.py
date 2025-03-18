"""
CPF: 746.824.890-70
COlete a soma dos 9 primeiros digitos do CPF
multiplicado cada um dos valores por uma contagem regressiva começando por 10

Ex: 746.824.890-70 (74682489070)
7*10 5*9 6*8 8*7 2*6 4*5 8*4 9*3 0*2

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado da soma por 10
301 * 10 = 3010
Obter o resti da divisão da conta anterior por 11
3010 % 11 = 7
Se o reultado for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro digito do cpf é 7
"""

cpf = input('Digite o seu cpf: ').replace('.', '').replace('-', '')
try:
    # lista_cpf_primeiro_digito = []
    # lista_cpf_segundo_digito = []
    # contador = 0
    # total_multplicacao_primeiro_numero = 0
    # total_multplicacao_segundo_numero = 0
    # for i in range(0, len(cpf)):
    #     contador += 1
    #     if contador < 10:
    #         lista_cpf_primeiro_digito.append(int(cpf[i]))
    #     elif contador < 11:
    #         lista_cpf_segundo_digito.append(int(cpf[i]))
    # if len(cpf) != 11:
    #     print(f'O seu cpf ({cpf}) tem menos que 11 números aceitos!')
    # else:
    #     for indice, numero in enumerate(lista_cpf_primeiro_digito):
    #         contador -= 1
    #         total_multplicacao_primeiro_numero += numero * contador    
    #     resto_divisao_primeiro_numero = total_multplicacao_primeiro_numero % 11
    #     if resto_divisao_primeiro_numero == 0 or resto_divisao_primeiro_numero == 1:
    #         primeiro_digito = 0
    #     else:
    #         primeiro_digito = 11 - resto_divisao_primeiro_numero 
    #     contador = 11
    #     for indice, numero in enumerate(lista_cpf_segundo_digito):
    #         total_multplicacao_segundo_numero += numero * contador
    #         contador -= 1
    #     resto_divisao_segundo_numero = total_multplicacao_segundo_numero % 11
    #     if resto_divisao_segundo_numero == 1 or resto_divisao_segundo_numero == 0:
    #         segundo_digito = 0
    #     else:
    #         segundo_digito = 11 - resto_divisao_segundo_numero
    soma_primeiro = 0
    for i in range(9):
        soma_primeiro += int(cpf[i]) * (10 - i)
    resto_primeiro = soma_primeiro % 11
    primeiro_digito = 0 if resto_primeiro < 2 else 11 - resto_primeiro

    soma_segundo = 0
    for i in range(10):
        soma_segundo += int(cpf[i]) * (11 - i)
    resto_segundo = soma_segundo % 11
    segundo_digito = 0 if resto_segundo < 2 else 11 - resto_segundo
    digitos_final = f"{primeiro_digito}{segundo_digito}"
    verificacao = cpf[-2:]
    if digitos_final == verificacao:
        print('O seu cpf é válido!')
    else:
        print('O seu cpf não é válido!')   
except ValueError:
    print(f' O seu {cpf} é inválido!')