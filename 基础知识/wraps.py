"""
    装饰器练习：
    装饰器的目的：不改变原函数增加功能
    装饰器写法：一个函数用被装饰的函数作为参数，返回一个内部函数，内部函数需要能接收被装饰函数的参数并返回被装饰函数的执行结果
    装饰器使用：语法糖@wraps  完全等价于  func = wraps（func)
    带参数的装饰器：再增加一层包装为装饰器接收参数, 根据嵌套函数先执行外面再执行里面的顺序，最外层接收参数，中层接收函数，
            内层增加被装饰函数的功能
    多个装饰器顺序：
    已有的装饰器对被装饰函数有要求么？
"""


def deco(func):
    """
    装饰器，将原函数的返回值翻倍
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        print("函数结果翻倍！")
        r = func(*args, **kwargs)
        return r * 2
    return wrapper


@deco
def test(n):
    print(n)
    return n * 2


def main():
    num = 3
    re = test(num)
    print("result is :", re)


if __name__ == '__main__':
    main()
