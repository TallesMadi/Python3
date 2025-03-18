lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Talles'}
]

for item in lista:
    if isinstance(item, set):
        print('SET')
        print(item, isinstance(item, set)) # é instância de ...
    elif isinstance(item, str):
        print('STR')
        print(item.upper())
    elif isinstance(item,(float, int)):
        print('NUM')
        print(item)
    else:
        print('OUTRO')
        print(item)