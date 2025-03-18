"""
Faça uma lista de compar com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""
import os

lista_de_compras = []

while True:
    opcao = input('Selecione uma opção\n[i]inserir [a]apagar [l]listar [s]sair: ').lower()
    if opcao == 'i':
        valor_inserido = input('Valor a ser inserido: ').capitalize()
        lista_de_compras.append(valor_inserido)
    elif opcao == 'a':
        indice_inserido = input('Informe um índice para ser apagado: ')
        try:
            indice_inserido_int = int(indice_inserido)
            if indice_inserido_int <= len(lista_de_compras):
                print(f'Apagou {lista_de_compras[indice_inserido_int]} da lista')
                lista_de_compras.pop(indice_inserido_int)
            else: 
                print(f'O índice {indice_inserido_int} não está detro do range da lista de compras')
        except ValueError:
            print(f'O valor {indice_inserido} não é um núemro inteiro')
        except Exception:
            print(f'O valor {indice_inserido} não é um valor válido como índice')
    elif opcao == 'l':
        if len(lista_de_compras) > 0:
            for indice, nome in enumerate(lista_de_compras):
                print(indice, nome)
        else:
            print('A lista não possui dados ainda!')
    elif opcao == 's':
        print('Fechando lista!')
        break
    else:
        print(f'O valor "{opcao}" inserido é inválido!')
