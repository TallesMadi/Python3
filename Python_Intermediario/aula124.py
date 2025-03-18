# Problemas dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('Talles')
adiciona_clientes('Raquel', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Luna')
adiciona_clientes('Totó', cliente2)
print(cliente2)