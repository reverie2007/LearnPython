#! /usr/bin/env python3
"""
    练习迭代器的使用及编写
"""


def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step


g = frange(0, 20, 4)
print(g)
print(next(g))


def gen_infinet():
    x = 0
    while True:
        yield x
        x += 1


g2 = gen_infinet()

for i in g2:
    print(i)
    if i > 5:
        break
