#f-strings
nome = 'Talles'
peso = 90
altura = 1.95
numero_grande = 100000000.4

imc = peso / altura ** 2
print(f'O IMC de {nome} é igual a: {imc:.2f}') # :.2f = duas casas decimais
print(f'{numero_grande:,.2f}')