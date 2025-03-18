"""
while e continue
"""

contador = 0

while contador < 50:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6')
        continue

    if 10 <= contador <= 27:
        continue

    print(contador)
