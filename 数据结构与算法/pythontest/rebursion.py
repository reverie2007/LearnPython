"""
    递归Rebursion
    python默认最高支持1000层递归
"""
import sys


def sum_list(num_list: list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        num = num_list.pop()
        return num + sum_list(num_list)


def sum_list_tail(total: int, num_list: list):
    """
    这样是尾调用么？空间与栈的使用有啥变化，如何观察检测？
    python不支持尾递归，因为这很不Pythonic.

    :param total:
    :param num_list:
    :return:
    """
    if len(num_list) == 1:
        return total + num_list[0]
    else:
        return sum_list_tail(total + num_list.pop(), num_list)


def main():
    print('最大递归调用层数：', sys.getrecursionlimit())
    print(sum_list_tail(0, list(range(100))))


if __name__ == '__main__':
    main()
