# Funções decoradoras e decoradores com classes
def add_repr(cls):
    def my_repr(self):
        class_name = type(self).__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = my_repr
    return cls

def my_planet(metodo):
    def intern(self, *args, **kwargs):
        result = metodo(self, *args, **kwargs)
        if 'terra' in result.lower():
            return 'Você está em casa'
        return result
    return intern

@add_repr
class Country:
    def __init__(self, nome):
        self.nome = nome

@add_repr
class Planet:
    def __init__(self, nome):
        self.nome = nome

    @my_planet
    def call_name(self):
        return f'O planeta é {self.nome}'

# Country = add_repr(Country) # igual a @add_repr
brasil = Country('Brasil')
portugal = Country('Portugal')

# Planet = add_repr(Planet)
terra = Planet('Terra')
marte = Planet('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)

print(terra.call_name())
print(marte.call_name())