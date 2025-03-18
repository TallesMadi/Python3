palavra = 'felicidade'
senha = '*'*len(palavra)
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
numero_tentativas = 0

print('Tente advinhar a palavra, você possui 5 tentativas')

while '*' in senha:
    print(senha)
    numero_tentativas += 1
    letra_usuario = input('Escolha uma letra para adivinhar a palavra: ')
    if len(letra_usuario) == 1 and letra_usuario in alfabeto:
        for i in range(0, len(palavra)):
            if palavra[i] is letra_usuario:
                senha += letra_usuario
            elif senha[i] in alfabeto:
                senha += senha[i]
            else:
                senha += '*'
    else:
        print(f'Você digitou uma palavra ou um número: {letra_usuario}')
        continue
    senha = senha[len(palavra):]
print(f'Você adivinhou a palavra {palavra} em {numero_tentativas} tentativas')