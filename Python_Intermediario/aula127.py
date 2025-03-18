import json

caminho = 'C:\\Python3\\Python_Intermediario\\aula127.json'

def listar(tarefas):
    if not tarefas:
        print('Não há nada para listar!')
        return  
    
    print('TAREFAS:')
    for item in tarefas:
        print(f'\t{item}')

def desfazer(tarefas, refazer):
    if not tarefas:
        print('Não há nada para desfazer!')
        return
    refazer.append(tarefas[-1])
    tarefas.pop()

def refazer(tarefas, refazer):
    if not tarefas:
        print('Não há nada para refazer!')
        return
    
    tarefas.append(refazer[-1])
    refazer.pop()

def adicionar(tarefa, tarefas):
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)

def salvar(tarefas):
    if tarefas:
        with open(caminho, 'w+', encoding='utf-8') as arquivo:
            json.dump(
                tarefas,
                arquivo, 
                ensure_ascii=False,
                indent=2
            )
        print('Lista Salva')
        return
    print('Lista vazia, não pode ser salva!') 

lista_tarefas = []
lista_refazer = []

while True: 
    item = input('Comandos: Listar, dezfazer, refazer e salvar\nColoque uma tarefa nova ou use um comando: ')
    if item.lower() == 'listar':
        listar(lista_tarefas)
    elif item.lower() == 'desfazer':
        desfazer(lista_tarefas, lista_refazer)
    elif item.lower() == 'refazer':  
        refazer(lista_tarefas, lista_refazer)
    elif item.lower() == 'salvar':
        salvar(lista_tarefas)
        break
    else:
        adicionar(item, lista_tarefas)
    print('\n')