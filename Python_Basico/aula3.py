"""
Python = Linguagem de programação
Tipo de tipagem (tipos de dados) = Dinâmica / Forte
Dinâmica = percebe o tipo de um dado sem a necessidade
do usuário a especificar
str -> string -> texto
Forte = não permite conversões implícitas 
Ex: x = '10'
y = 2
print(x + y) # Erro de concatenação
Interpretador lê da esquerda para direita, de cima para baixo
Strings são textos que estão dentro de aspas
"""

# Aspas Simples
print('Talles Madi')

# Aspas Duplas
print("Talles Madi")

# Escape
print("Talles \"Madi\"")
# o caracter depois da barra invertida (\) não será interpretado

# r
print(r"Talles \"Madi\"")
# mostra todos os caracteres, feito para expressões regulares

#truque
print("Talles 'Madi'")
print('Talles "Madi"')
