"""
Calculadora com while
"""
print('Calculadora')
while True:
    numero1 = input('Digite o primeiro número: ')
    numero2 = input('Digite o segundo número: ')
    operacao = input('Agora esolha qual operação: \n1 = adição\n2 = subtração\n3 = mutiplicação\n4 = divsão\n')
    try:
        float_numero1 = float(numero1)
        float_numero2 = float(numero2)
        int_operacao = int(operacao)
        if int_operacao == 1:
            resultado = float_numero1 + float_numero2
        elif int_operacao == 2:
            resultado = float_numero1 - float_numero2 
        elif int_operacao == 3:
            resultado = float_numero1 * float_numero2
        elif int_operacao == 4:
            resultado = float_numero1 / float_numero2
        else: 
            print(f'Você digitou o valor {operacao} da operação errado')
        print(resultado)      
    except:
        print(f'Você digitou algum valor ({numero1}, {numero2} ou {operacao}) inválido')
    sair_entrar = input('Quer continuar? S/n ').lower().startswith('n')
    if sair_entrar:
        print('Você saiu do programa!')
        break