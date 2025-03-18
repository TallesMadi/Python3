# Variável livre + nonlocal (locals, globals)

def fora(x):
    a = x

    def dentro():
        # print(dentro.__code__.co_freevars)
        print(locals())
        return a
    return dentro

dentro = fora(7)
print(dentro())

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_concatenar):
        nonlocal valor_final
        valor_final += valor_concatenar
        return valor_final
    return interna

concat = concatenar('a')
print(concat('mor'))
print(concat('oso'))
print(concat('s'))

