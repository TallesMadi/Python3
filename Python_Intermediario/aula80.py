# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

respostas = []
for i in range(len(perguntas)):
    respostas += [perguntas[i].popitem()]

contador = 0
acertos = 0
for nome in perguntas:
    resposta_atual = respostas[contador][1]
    print(nome['Pergunta'])
    opcoes = nome['Opções']
    print('Alternativas: ')
    print(f'({opcoes[0]}) ({opcoes[1]}) ({opcoes[2]}) ({opcoes[3]})')
    valor_usuario = input('Digite a sua resposta: ')
    if valor_usuario == resposta_atual:
        print('Você acertou!')
        acertos += 1
    elif valor_usuario not in opcoes:
        print('Você não digitou nenhuma das alternativas!')
    else: 
        print(f'Você errou! A resposta era {resposta_atual}.')
    contador += 1

print(f'Você acertou {acertos} de um total de {contador} perguntas')