"""
    计算质数
    计算方法：埃氏筛法步骤
    构建自然数列
    先把1删掉
    取出最小的2，把2的倍数删掉
    取出最小的3，把3的倍数删掉
    取出最小的5，把5的倍数删掉
    以此类推

    python可以方便的使用生成器与筛选函数构建‘懒惰’数列，节省存储空间
    思考：面对一个无限序列，删除操作是如何进行的？
    这个算法的空间复杂度与时间复杂度？

"""


def _odd_iter():
    """
    3开头的奇数数列
    :return:
    """
    num_odd = 3
    while True:
        yield num_odd
        num_odd = num_odd + 2


def _not_divisible(num):
    """
    返回一个判断函数，用来判定自然数n能否被指定的数整除。
    :param num:
    :return:
    """
    return lambda x: x % num > 0


def primes():
    yield 2
    prime_iter = _odd_iter()
    while True:
        num = next(prime_iter)
        yield num
        prime_iter = filter(_not_divisible(num), prime_iter)


if __name__ == '__main__':
    for n in primes():
        if n > 11000:
            break
        elif n > 10900:
            print(n)
