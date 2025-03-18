# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

class CarrinhoDeCompras:
    def __init__(self):
        self._produtos = []

    def preco_total(self):
        return sum(p.preco for p in self._produtos)

    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

    def inserir_produtos(self, *produtos):
        # for produto in produtos:
        #     self._produtos.append(produto)
        # -----
        # self._produtos += produtos
        self._produtos.extend(produtos)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = CarrinhoDeCompras()
p1, p2, p3 = Produto('Carta Pokémon', 10), Produto('Sleeve', 0.2), Produto('Fichário Pokémon', 150)

carrinho.inserir_produtos(p1, p2, p3)
carrinho.listar_produtos()
print(carrinho.preco_total())