numero = input('Digite um número inteiro: ')

try:
    if numero.isdigit:
        int_numero = int(numero) 
        if int_numero % 2 == 0:
            print(f'O número inteiro {numero} é par')
        else:         
            print(f'O número inteiro {numero} é impar')
except:
    print(f'O valor {numero} não é um numero inteiro')