from itertools import count
# count é um iterador sem fim (itertools)

c1 = count()
# c1 = count(10, 10) começa no 10, de 10 em 10
r1 = range(100)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print('Count')
for i in c1:
    if i >= 100:
        break
    print(i)

print('-'*40)
print('Range')
for i in r1:
    print(i)
