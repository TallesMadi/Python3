# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        arquivo = open(caminho_arquivo, modo, encoding='utf-8')
        yield arquivo
    # except Exception as e:
    #     print('Oorreu erro', e)
    finally:
        arquivo.close()

with my_open('C:\\Python3\\Python_POO\\aula159.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 11)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)