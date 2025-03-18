# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
def não_aceito_zero(divisor):
    if divisor == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero!')
    return True

def deve_ser_int_ou_float(numero):
    tipo_n = type(numero)
    if not isinstance((numero), (int, float)):
        raise TypeError(
            f'{numero} deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado'
        )
    return True

def divide(numero, divisor):
    deve_ser_int_ou_float(numero)
    deve_ser_int_ou_float(divisor)
    não_aceito_zero(divisor)    
    return numero / divisor

print(divide(True, 0))