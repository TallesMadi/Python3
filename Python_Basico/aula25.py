"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r (__repr__) !s (__str__) !a (__ascii__)
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >6}')
print(f'{variavel: <6}.')
print(f'{variavel: ^6}')
print(f'{variavel:-<6}')
print(f'{10000.29342776434576224:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
