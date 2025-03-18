class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str: 
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)
    
    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return True if resultado_self > resultado_other else False 


if __name__ == '__main__':
    ponto1 = Ponto(1, 4)
    ponto2 = Ponto(3, 7)
    ponto3 = ponto1 + ponto2
    print(ponto3)
    print('Ponto 1 é maior que o ponto 2? ', ponto1 > ponto2)
    print('Ponto 2 é maior que o ponto 1? ', ponto2 > ponto1)
