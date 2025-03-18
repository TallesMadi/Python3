"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Talles', 'Raquel', 1, True, 1.2]
lista_b = lista_a.copy()
lista_a[3] = False
lista_b[2] = 7
print(lista_a, lista_b)