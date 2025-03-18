"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[-1])
print(variavel[4:])#quando se omite ele vai até o final ou o começo
print(variavel[:4])
print(len(variavel))
print(variavel[0:len(variavel):2])
print(variavel[::1])
print(variavel[::-1])
