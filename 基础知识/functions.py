"""
    思考以下问题：
    函数参数可变对象与不可变对象表现有哪些不同
    不定数量的函数参数
    可迭代对象解包传递
    赋值语句使用*号代表不同数量变量与参数使用*的区别
"""


def using_list(list1):
    """
    如果传入一个list，在函数中修改后，原来的值也跟着变化
    :param list1: List
    :return:
    """
    for k, v in enumerate(list1):
        list1[k] = v * 2


def test_list():
    """

    :return:
    """
    list1 = [i for i in range(1, 11)]
    print(list1)
    using_list(list1)
    print(list1)


def using_func(func1):
    """函数作为参数传递，修改

    """
    print(func1)
    func1 = using_list
    return func1


def test_func():
    f1 = test_func
    print(f1, type(f1))
    using_func(f1)
    print(f1, type(f1))
    f1 = using_func
    print(f1, type(f1))


def main():
    test_list()
    test_func()


if __name__ == '__main__':
    main()
