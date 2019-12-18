"""
    生成器next与send
"""


def gen():
    for j in range(10):
        print('i = ', j)
        num = yield j
        print('num = ', num)


if __name__ == '__main__':
    g = gen()
    n = 100
    for i in range(5):
        m = next(g)
        print("next获取值:", m)

    for i in range(5):
        m = g.send(n + i)
        print("send获取值：", m)
