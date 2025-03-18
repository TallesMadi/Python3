"""
Exercícios
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetros
"""

def criar_multiiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiiplicador(2)
triplicar = criar_multiiplicador(3)
quadruplicar = criar_multiiplicador(4)

for numero in [1, 2]:
    print(duplicar(numero))
    print(triplicar(numero))
    print(quadruplicar(numero))
    print('-'*10)
    