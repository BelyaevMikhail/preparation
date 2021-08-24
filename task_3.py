import random


def gen(start, finish):
    spisok = []
    slovar = {}
    for _ in range(10):
        rnd = int((finish - start) * random.random() + start)
        spisok.append(rnd)
        slovar.update({'elem_{}'.format(rnd): rnd})

    return (spisok, slovar)


print(gen(7, 26))
