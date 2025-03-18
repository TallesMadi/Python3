nome_usuario = input('Digite seu nome: ')

tamanho_nome_usuario = len(nome_usuario)

if 1 <= tamanho_nome_usuario <= 4:
    print(f'O seu nome {nome_usuario} é curto demais, possui {tamanho_nome_usuario} letras!!')
elif 5 <= tamanho_nome_usuario <= 6:
    print(f'O seu nome {nome_usuario} é tem um tamanho normal, possui {tamanho_nome_usuario} letras!!')
elif tamanho_nome_usuario > 6:
    print(f'O seu nome {nome_usuario} é muito grande, possui {tamanho_nome_usuario} letras!')
else:
    print('Você não inseriu nome de usuário!')