"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
# condicao = 10 == 10
# variavel= 'Valor' if condicao else 'Outro valor'
# print(variavel)

digito = 9
novo_digito = digito if digito <=9 else 0
novo_digito_inverso = 0 if digito > 9 else digito
print(novo_digito, novo_digito_inverso)

print('Valor' if False else 'Valor2' if False else 'Valor3')