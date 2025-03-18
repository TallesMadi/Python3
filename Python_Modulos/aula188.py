# random tem geradores de números pseudoaleatórios
# Obs.: números pseudoaleatórios significa que os números
# parecem ser aleatórios, mas na verdade não são. Portanto,
# este módulo não deve ser usado para segurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
# a saída pode ser previsível.
# doc: https://docs.python.org/pt-br/3/library/random.html
import random
import time

# Funções:
# seed
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
random.seed(time.time())

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10, 20, 2)
print(f'Um número aleatório entre 10 e 20, de 2 em 2: {r_range}')
print('#'*10)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
print(f'Um número aleatório entre 10 e 20: {r_int}')
print('#'*10)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
print(f'Um número flutuante entre 10 e 20: {r_uniform}')
print('#'*10)

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['Talles', 'Raquel', 'Luna', 'Ash']
random.shuffle(nomes)
print(f'Embaralha uma lista: {nomes}')
print('#'*10)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=2)
print(nomes)
print(novos_nomes)
print('#'*10)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=4)
print(nomes)
print(novos_nomes)
print('#'*10)

# random.choice(Iterável) -> Escolhe um elemento do iterável
print('Escolhe um item de uma lista: ', random.choice(nomes))