"""
Introdução às funções (def) em Python
funções são trechos de código usados para replicar determinada ação ao longo do seu código. 
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
Por padrão, funções python retornam None (nada)
"""

def somar(a, b, c): # parâmetros = a, b, c
    soma = a + b + c
    return soma

def saudacao(nome='Sem nome'):
    print(f'Olá, {str(nome).capitalize()}!')

print(somar(7, 28, 69))
saudacao('talles')
saudacao()