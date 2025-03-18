"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um código não tem fim
"""

while True:
    nome = input('Qual o seu nome: ').capitalize()   
    if nome == 'Sair':
        break
    else:
        print(f'Seu nome é {nome}')