# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe

class A:
    def __new__(cls, *args, **kwargs):
        instancia = super().__new__(cls)
        instancia.x = 'Pokemon'
        return instancia

    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return f'{self.__class__.__name__}()'
    
a = A('Metallica')
print(a.x)
# a = object.__new__(A) 
# a.__init__()
