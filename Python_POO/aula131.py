#  Escopo da classe e de métodos da classe

class Animal:
    def __init__(self, nome):
        self.nome = nome.capitalize()
        # variavel = 'valor' 
        # print(variavel)
    def comer(self, alimento):
        return f'{self.nome} está comendo {alimento}!'

leao = Animal('Leão')
print(leao.nome)
print(leao.comer('Feijão Tropeiro'))