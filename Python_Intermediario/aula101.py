# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O python conhece todos os módulos e pacotes presentes nos caminhos de sys.path
# import sys
# print(*sys.path, sep='\n')

import aula101_m
# from aula101_m import nome, revere_word

print(aula101_m.reverse_word(aula101_m.nome))
print('Este módulo se chama', __name__)