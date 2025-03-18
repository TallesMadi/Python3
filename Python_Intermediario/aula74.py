"""
Higher Order Functions
Funções de primeira ordem
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

# saudacao_2 = saudacao
v = executa(saudacao, 'Bom dia', 'Talles')
print(v)