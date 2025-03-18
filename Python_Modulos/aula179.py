# os.listdir para navegar em caminhos
import os

caminho = os.path.join('\\Python3')
print(caminho)

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(caminho_completo_pasta)
    if not os.path.isdir(caminho_completo_pasta):
        continue
    for item in os.listdir(caminho_completo_pasta):
        print('    ', item)

