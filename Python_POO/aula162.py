# Classes decoradoras (decorator classes)
class Multiplicar:
    def __init__(self, func):
        self.func = func
        self._multiplicador = 10

    def __call__(self, *args, **kwds):
        resultado = self.func(*args, **kwds)
        resultado *= self._multiplicador
        return resultado

@Multiplicar
def soma(x, y):
    return x + y

print(soma(2, 5))