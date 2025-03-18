#  Introdução as Generator functions em Python
#  generator = (n for n in range(1000000))

#toda função com yield é uma generator function
def generator(n=0, maximum=10):
    while True:
        yield n # pausa execução
        n += 1
        if n > maximum:
            return

gen = generator(maximum=100000)

for n in gen:
    print(n)
