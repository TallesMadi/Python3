# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os, aula181
from itertools import count

caminho = os.path.join('\\Python3')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    # print(the_counter, 'Pasta Atual',root)

    for dir_ in dirs:
        # print('    ', the_counter, 'Dir:', dir_)
        for file_ in files:
            caminho_completo_arquivo = os.path.join(root, file_)
            # stats = os.stat(caminho_completo_arquivo)
            # tamanho = stats.st_size
            tamanho = os.path.getsize(caminho_completo_arquivo)
            print('        ', the_counter, 'File:', file_, aula181.size_format(tamanho))

        
