"""
    python基础知识学习
"""


def inteager_size():
    """
    python整数是无限大小的？
    :return:
    """
    num = 56445613245679874654653132454564
    for i in range(10):
        num *= num
        print(num)
    # 很大的整数除法得到的结果是什么？普通除法会报错，即使能整除返回结果也是一个float，整除和取余正常
    num2 = num / 56445613245679874654653132454564
    print(num2)


def test_change(list1, list2):
    # 测试传递过来的可变对象list
    for e in list1:
        print(type(e))
        e = 100
        print(type(e))
    print('list1 =', list1)
    list1[0] = 100  # 思考e = list[0];e=100与list[0] = 100的差别
    print('list1 =', list1)
    print('param list2 id =', id(list2))


def test_id():
    # 对不可变类型，如int，值相同的变量可能会也可能不会指向相同的对象，这取决于具体实现
    a = 1
    b = 1
    print('id(a) = ', id(a))
    print('id(b) =', id(b))
    # 对可变类型，如列表，变量绝不会指向相同的对象
    c = []
    d = []
    print('id(c) =', id(c))
    print('id(d) =', id(d))
    e = c
    print('id(e) =', id(e))
    l1 = [[1], 2, 3]
    l2 = [4, 5, 6]
    print('l2 id =', id(l2))
    test_change(l1, l2)
    print('l1 =', l1)
    print('l2 =', l2)


if __name__ == '__main__':
    # test_id()
    nums = [1, 2, 3]
    print(nums[:0])
    print(nums[:1])
    print(nums[1:])
    print(nums[3:])
    print(nums[4:])
