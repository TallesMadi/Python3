#  __dict__ e vars para atributos de instância
import copy
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        # return self.ano_atual - self.idade
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Talles', 20)
p2 = Pessoa('Raquel', 22)

print(p1.__dict__)
print(vars(p1))

print(p2.__dict__)
print(vars(p2))

dictionary = copy.deepcopy(vars(p1))
print(dictionary)