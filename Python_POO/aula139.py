# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
        self.ponta = None

    @property
    def cor(self):
        return self.cor_tinta

    @property
    def tamanho_ponta(self):
        return 0.5

    def get_cor(self):
        return self.cor_tinta

c1 = Caneta('Vermelha')
c2 = Caneta('Azul')

print(c1.get_cor())
print(c2.get_cor())
print('-'*10)
print(c1.cor_tinta)
print(c2.cor_tinta)
print(c1.tamanho_ponta)
print(c2.tamanho_ponta)