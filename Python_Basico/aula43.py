frase = 'O python é uma linguagem de programação multiparadigma. O python foi criado por Guido van Rossum.'.lower()

indice = 0
letra_favorita = ''
quantidade_letra_favorita = 0

while indice < len(frase):
    letra_atual = frase[indice]
    quantidade_letra_atual = frase.count(letra_atual)

    if  quantidade_letra_atual > quantidade_letra_favorita and letra_atual != ' ':
        letra_favorita = frase[indice]
        quantidade_letra_favorita = quantidade_letra_atual

    indice += 1
print(f'A letra aparece mais vezes na frase é "{letra_favorita}", aparecendo {quantidade_letra_favorita} vezes!')

