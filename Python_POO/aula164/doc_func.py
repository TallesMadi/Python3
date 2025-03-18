"""Este é um modulo e exemplo

Este módulo contém funções e exemplos de documentação de documentação  de funções.
"""

def soma(x: int | float, y: int | float) -> int | float:
    """Soma entre dois números, x e y"""
    return x + y

def multiplica(x: int | float, y: int | float, z: int | float | None = None) -> int | float:
    """Multiplica x, y e/ou z
    Multiplica x e y. Se z for enviado, multiplica x, y, z.
    """
    if z is not None:
        return x * y * z
    return x * y