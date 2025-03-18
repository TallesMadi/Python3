# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Mover/Renomear -> shutil.move
# Mover/Renomear -> os.rename
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar -> os.unlink
# Apagar diretório recursivamente -> shutil.rmtree 
import os, shutil

# NÃO EXECUTAR ESTE CÓDIGO

HOME = os.path.expanduser('~')
ONEDRIVE = os.path.join(HOME, 'OneDrive')
PASTA_ORIGINAL = os.path.join(ONEDRIVE, 'EXEMPLO')
NOVA_PASTA = os.path.join(ONEDRIVE, 'NOVA_PASTA')

# shutil.rmtree(NOVA_PASTA, ignore_errors=True)
# shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)

# os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        novo_caminho_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
            )
        # os.makedirs(NOVA_PASTA, exist_ok=True)
    for file in files:
        caminho_arquivo = os.path.join(root, file)
        novo_caminho_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
            )
        print(novo_caminho_arquivo)
        shutil.copy(caminho_arquivo, novo_caminho_arquivo)
