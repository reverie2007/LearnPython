"""
    生成器，思考以下问题：
    函数中多个yield： 每到一个yield暂停返回一次
    yield from
    scrapy中处理函数要求是yield返回，如果没有yield或者使用return返回是什么情况呢？
"""
import types


class Parent:
    def gen_num(self):
        for i in range(10):
            yield i

    def say(self):
        nums = self.gen_num()
        for i in nums:
            print(i)


class Child(Parent):
    def gen_num(self):
        yield 3


def count_down(n):
    print("start count from: ", n)
    """
    while n > 0:
        yield n
        n -= 1
    yield -1
    print("Done!")
    """
    return -2


def main():
    print(type(count_down))
    gen = count_down(3)
    print(type(gen))
    if isinstance(gen, types.GeneratorType):
        for i in gen:
            print(i)


def main2():
    p = Child()
    p.say()


if __name__ == '__main__':
    main2()
