"""
Operadores in e not in
Strings são iteráveis (pode navegar item por item)
 0 1 2 3 4 5 (índices)
 t a l l e s
-6-5-4-3-2-1 (índices negativos)
"""
nome = 'Talles'
print(nome[-6])
print('z' not in nome)
print('z' in nome)

palavra = input('Digite uma palavra: ')
encontrar = input('Digite o que deseja encontrar na sua palavra: ')

if encontrar in palavra:
    print(f'Existe {encontrar} na sua palavra!')
else:
    print(f'Não existe {encontrar} na sua palavra!')
