lista_1 = []
for i in range(3):
    for j in range(3):
        lista_1.append((i, j))
# print(lista_1)

lista_2 = [
    (x, y) for x in range(3)
    for y in range(3) 
]
# print(lista_2)


lista_3 = [
    [[x, letra] for letra in 'Talles']
    for x in range(3) 
]
print(lista_3)
