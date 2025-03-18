#  Métodos em instâncias em classes Python
#  Hard Coded = é algo que foi diretamente escrito no código  
# Instância da class (objeto) - Tem os dados
#  Uma classe pode gerar várias instâncias
#  Na classe o self é a própria instância

class Carro:
    def __init__(self, nome, marca):
        # self.nome = 'Gol' - Hard coded
        self.nome = nome 
        self.marca = marca
    def acelerar(self):
        print(f'{self.nome} está acelerando')

uno = Carro('Uno', 'Fiat')
print(uno.nome, uno.marca)

uno.acelerar()
Carro.acelerar(uno)

civic = Carro('Civic', 'Honda')
print(civic.nome, civic.marca)
