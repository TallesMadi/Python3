# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

def recursiva(inicio=0, fim=10):
    # caso base
    if inicio >= fim:
        return fim
    # Caso recursivo
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())

def fatorial(numero):
    if numero <= 1:
        return 1
    return numero * fatorial(numero - 1)

print(fatorial(5))

# fatorial = 5
# for c in range(fatorial - 1, 0, -1):
#     fatorial *= c

# print(fatorial)