# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(f'{endereco.rua} - {endereco.numero}')

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print(f'Apagando {self.rua} - {self.numero}')

cliente1 = Cliente('Talles')
cliente1.inserir_endereco('Rua dos Milagres', 66)
cliente1.inserir_endereco('Rua de Deus', 33)
cliente1.listar_enderecos()
