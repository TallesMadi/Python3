# if, elif e else
# se, se não se e se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou!')
elif entrada == 'sair':
    print('Você saiu!')
else:
    print('Você não digitou "entrar" nem "sair"!')

condicao = True

if condicao: #se vc apenas escrever a variavel, será verificado se é verdadeiro
    print('Este é o código if')
else:
    print('Esse é o código do else')