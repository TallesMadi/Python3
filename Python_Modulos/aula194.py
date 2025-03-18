# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá, Mundo" na tela',
    type=str, # se action for ativado, desativar esse
    metavar='STRING',
    default='Olá, Mundo!',
    required=False,
    nargs='+',
    # action='append' #recebe o argumento mais de uma vez
)
args = parser.parse_args()

if args.basic is None:
    print('Voce não passou o valor de "b"')
else:
    print('O valor de b:', args.basic)