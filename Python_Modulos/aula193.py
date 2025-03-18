# sys.argv - Executando arquivos com argumentos no sistema 
import sys

args = sys.argv
quantity_args = len(args)

if quantity_args <= 1:
    print('Você não passou argumentos')
else:
    print(f'Voce passou {quantity_args - 1} argumentos: {args[1:]}')