# exemplo do uso de sets
letras = set()
while True:
    letra = input('Digite: ')   
    if len(letra) != 1:
        print('Digite apenas uma letra!')
    else:
        letras.add(letra.lower())
        print(letras)
