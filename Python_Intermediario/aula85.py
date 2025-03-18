def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

print(executa(lambda x, y: x + y, 7, 13))
#  lambda parametro: retorno

def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplica = executa(lambda m: lambda n: n * m, 2)

print(duplica(7))

print(executa(lambda *args: sum(args), 1, 2, 3, 4, 5, 6, 7))