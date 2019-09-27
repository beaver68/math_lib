import random


def is_sim(val):
    s = True
    for i in range(2, val//2 + 1):
        if val % i == 0:
            s = False
            break
    return [True if s else False]


def is_sim_tuple(lst):
    return list(zip(lst, [str(is_sim(i)) for i in lst]))


lst_1 = [random.randint(1, 100) for i in range(random.randint(1, 15))]
print(is_sim_tuple(lst_1))








