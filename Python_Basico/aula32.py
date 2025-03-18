horario_completo = input('Digite a hora atual (Ex: 12:30): ')

try:
    horas = int(horario_completo[0:2])
    if 0 <= horas <= 11:
        print('Bom dia!')
    elif 12 <= horas <= 17:
        print('Boa tarde!')
    elif 18 <= horas <= 23:
        print('Boa noite!')
    else:
        print('O horário inserido está incorreto!')
except:
    print(f'O valor {horario_completo} não segue o padrão de horário!')