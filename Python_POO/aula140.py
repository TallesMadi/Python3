# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯
class Caneta:
    def __init__(self, cor):
        # protected 
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        if isinstance(valor, str):
            self._cor = valor   
        else:
            raise ValueError('Só é aceto valores em String!')
    
    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor
c1 = Caneta('Verde')

# setter
c1.cor = 'Preto'
c1.cor_tampa = 'Dourado'

# getter
print(c1.cor)
print(c1.cor_tampa)
