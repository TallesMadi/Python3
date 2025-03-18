# secrets gera números aleatórios seguros
import secrets
import string as s
from secrets import SystemRandom as sr

print(''.join(sr().choices(s.ascii_letters + s.digits + s.punctuation, k=8)))

random = secrets.SystemRandom()

print(secrets.randbelow(100))
print(secrets.choice([7, 77, 777]))

print('-'*60)

r_int = random.randint(10, 20)
print(f'Um número aleatório entre 10 e 20: {r_int}')
print('-'*60)

r_uniform = random.uniform(10, 20)
print(f'Um número flutuante entre 10 e 20: {r_uniform}')
print('-'*60)

nomes = ['Talles', 'Raquel', 'Luna', 'Ash']

print('Escolhe um item de uma lista: ', random.choice(nomes))

print('-'*60)

