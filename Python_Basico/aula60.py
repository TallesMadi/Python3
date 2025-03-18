"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '     Olha só,        que coisa interessante'
lista_frases_inicio = frase.split(', ')

lista_frases = []
for i, frase in enumerate(lista_frases_inicio):
    lista_frases.append(lista_frases_inicio[i].strip())
    print(frase.strip()) # corta os espaços do começo e do fim da string
    # lstrip: espaços do começo
    # rstrip: espaços do fim

print(lista_frases)
print(frase.split())
print(lista_frases_inicio)

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)
