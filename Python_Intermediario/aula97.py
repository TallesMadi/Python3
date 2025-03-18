#   Try, except, else e finally

try:
    a = 7
    b = 0
    # print(b[1])
    c = a / b
except ZeroDivisionError as zero:
    print('Dividiu por 0', zero.__class__.__name__)
except NameError:
    print('Você não definiu a variável')
except (TypeError, IndexError) as error:
    print('Erro de tipo + index')
    print(error)
    print(error.__class__.__name__)
except Exception:
    print('Erro desconhecido!')
