# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
lista_tarefas = []
lista_refazer = []

while True: 
    item = input('Comandos: Listar, dezfazer e refazer\nColoque uma tarefa nova ou use um comando: ')
    if item.lower() == 'listar':
        if len(lista_tarefas) != 0:
            print('TAREFAS:')
            for item in lista_tarefas:
                print(item)
        else: 
            print('Não há nada para listar!')
    elif item.lower() == 'desfazer':
        if len(lista_tarefas) != 0:
            lista_refazer.append(lista_tarefas[-1])
            lista_tarefas.pop()
        else:
            print('Não há nada para desfazer!')
    elif item.lower() == 'refazer':  
        if len(lista_refazer) != 0:
            lista_tarefas.append(lista_refazer[-1])
            lista_refazer.pop()
        else:
            print('Não há nada para refazer!')
    else:
        lista_tarefas.append(item)
    print('\n')