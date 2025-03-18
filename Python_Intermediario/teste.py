lista = [1, 5, 2, 7, 3, 12, 0, 9, 32, 2, 5, 6, 9, 10]

def highest_number(lista: list) -> int:
    list_size = len(lista)
    biggest_number, i = 0, 0
    while i < list_size:
        if  lista[i] >= biggest_number:
            biggest_number = lista[i]
        i += 1
    return biggest_number

print(highest_number(lista))

def fatorial(number: int) -> int:
    fatorial = number
    for i in range(1, number):
        print(i)
        fatorial *= i
    return fatorial

print(fatorial(5))

exchenge_rates = {
    'BRL': {'USD': 0.17, 'EUR': 0.16},
    'USD': {'BRL': 5.89, 'EUR': 0.94},
    'EUR': {'BRl': 6.23, 'USD': 1.06}
}

def coin_converter(value: float, source_currency, target_currency):
    if source_currency == target_currency:
        return value
    try:
        value *= exchenge_rates[source_currency][target_currency]
        return value
    except KeyError:
        return None

print(coin_converter(1000, 'BRL', 'USD'))
