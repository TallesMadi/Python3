# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       só DEVE ser usado dentro da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.
from functools import partial

class Foo:
    def __init__(self):
        self.public = 'Isso é público'
        self._protected = 'Isso é protegido'
        self.__private = 'Isso é privado'

    def metodo_publico(self):
        return 'Método Público'
    
    def _metodo_protegido(self):
        return 'Método Protegido'
    
    def __metodo_privado(self):
        return 'Método Privado'

f = Foo()
print(f.public)
print(f.metodo_publico())

# errado, não usar protected ou private fora da classe
# print(f._protected)
# print(f._metodo_protegido)