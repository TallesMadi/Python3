# Generator expression, Iterables (tem a responsabilidade de ter os valores) e Iterators (resposnabilidade de saber apenas qual é o proximo valor) em Python
import sys

iterable = ['Eu ', 'tenho ', '__iter__']
iterator = iterable.__iter__() # tem __iter__ e __next__
# iter(iterator)

for i in iterable:
    print(next(iterator))

lista = [n for n in range(10000)]
generator = (n for n in range(10000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for n in generator:
    print(n)