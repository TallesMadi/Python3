# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'palavra' # str
# print(string.capitalize())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

print(type(Pessoa))

p1 = Pessoa('Talles', 'Madi')
# p1.nome = 'Talles'
# p1.sobrenome = 'Madi'

print(p1.nome)
print(p1.sobrenome)

print('-' * 10)

p2 = Pessoa('Raquel', 'Manzato')
# p2.nome = 'Raquel'
# p2.sobrenome = 'Manzato'

print(p2.nome)
print(p2.sobrenome)
