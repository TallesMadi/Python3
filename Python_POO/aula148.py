# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class MinhaString(str):
    def upper(self):
        # retorno = super(MinhaString, self).upper() faz isso por baixo dos panos
        retorno = super().upper()
        return retorno

string1 = MinhaString('Talles')
print(string1.upper())

class A:
    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    def __init__(self, atributo, valor):
        super().__init__(atributo)
        self.valor = valor

    def metodo(self):
        super(B, self).metodo()
        print('B')

class C(B):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Usei args e kwargs')

    def metodo(self):
        super(C, self).metodo()
        # a partir do metodo C, procuro o metodo 'metodo'
        print('C')

c = C('Atributo', 'Valor')
print(c.atributo, c.valor)

c.metodo()
print(C.mro())