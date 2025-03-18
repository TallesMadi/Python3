"""
Funções decoradoras e decoradores
Decorar = Adicionar / Remover / Restringir / Alterar
Funções decoradoreas são funções para fazer o Python usar as funções decoradoras em outras funções
Decoradores são "Syntax Sugar"
"""
def criar_funcao(func): # função decoradora
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna

@criar_funcao # decorador
def inverte_string(string):
    print(f'{inverte_string.__name__}') # interna
    return string[::-1].lower()

def is_string(param):
    if not isinstance(param, str):
        raise TypeError(f'parametro "{param}" deve ser uma string')

invertida = inverte_string('67')
print(invertida)