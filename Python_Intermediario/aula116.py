from itertools import groupby
# groupby - agrupando valores (itertools)

alunos = [
    {'nome': 'Talles', 'nota': 'A'},
    {'nome': 'Luna', 'nota': 'B'},
    {'nome': 'Raquel', 'nota': 'A'},
    {'nome': 'Lucas', 'nota': 'C'},
    {'nome': 'Maria Flor', 'nota': 'D'},
    {'nome': 'Germano', 'nota': 'B'},
    {'nome': 'Carlos', 'nota': 'C'}
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)