# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(2))
print(multiplica_por_dez(2))

def criar_saudacao(saudacao):
    def nomear(nome):
        return f'{saudacao}, {nome}!'
    return nomear

saudar = criar_saudacao("Olá")
print(saudar("João"))

def criar_operacao(a, b, operacao):
    return lambda: operacao(a, b)


soma = criar_operacao(5, 3, lambda x, y: x + y)
print(soma()) 

def executar_condicional(numero):
    def verificador():
        if numero > 10:
            return 'Executando, pois o número é maior que 10'
        else: 
            return 'Número muito pequeno para executar'
    return verificador

funcao = executar_condicional(15)
print(funcao())

funcao = executar_condicional(8)
print(funcao())
