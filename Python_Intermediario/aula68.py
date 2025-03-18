"""
Argumentos nomeados e não nomeados
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y): # parâmetros = x, y
    print(f'{x=} + {y=} = {x + y}')

soma(1, 7) # argumentos posicionais = 1, 7
soma(y = 1, x = 7) # arguemtnos nomeados