"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

texto = 'Mirassol' # iterável

iterador = iter(texto) #__iter__()

while True:
    try:
        print(next(iterador)) #__next__()
    except StopIteration:
        break
