"""
Flag - Marcar um local
None = não valor
is e is not = é e não é (tipo, valor, identidade) 
id = identidade
"""
#id
variavel1 = 'a'
variavel2 = 'b'
print(id(variavel1))
print(id(variavel2))

#flags, is, not e none
condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Passou no if')
else:
    print('Não passou no if')

print(passou_no_if, passou_no_if is None, passou_no_if is not None)

if passou_no_if is None:
    print('Não passou no if')
if passou_no_if is not None:
    print('Passou no if')
    