"""
    基本排序算法

"""
from random import randint
from pythonds.basic.stack import Stack
import timeit
import math


# 冒泡法排序
def bubble_sort(a_list: list):
    """
    列表冒泡法排序
    :param a_list:
    :return:
    """
    for i in range(len(a_list) - 1, 0, -1):
        for j in range(i):
            if a_list[j] > a_list[j + 1]:
                # swap
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]


# 选择排序
def selection_sort(a_list: list):
    """
    选择排序（改进的冒泡排序，每次比较只需交换一次，交换次数减少）
    :param a_list:
    :return:
    """
    for i in range(len(a_list) - 1, 0, -1):
        pos_max = 0
        for j in range(1, i + 1):
            if a_list[j] > a_list[pos_max]:
                pos_max = j
        # swap
        a_list[pos_max], a_list[i] = a_list[i], a_list[pos_max]


# 插入排序
def insert_sort(a_list: list):
    """
    插入排序
    :param a_list:
    :return:
    """
    for i in range(1, len(a_list)):
        tmp_num = a_list[i]
        done = False
        j = i
        while j > 0 and not done:
            if a_list[j - 1] > tmp_num:
                a_list[j] = a_list[j - 1]
                j -= 1
            else:
                a_list[j] = tmp_num
                done = True
        if not done:
            a_list[0] = tmp_num


#  归并排序
def merge_sort(a_list: list):
    """
    归并排序
    :param a_list:
    :return:
    """
    if len(a_list) > 1:
        split_point = len(a_list) // 2
        left = a_list[:split_point]
        right = a_list[split_point:]
        # 左右分别排序
        merge_sort(left)
        merge_sort(right)

        # 合并左右两边
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a_list[k] = left[i]
                i += 1
            else:
                a_list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            a_list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a_list[k] = right[j]
            j += 1
            k += 1


def fast_sort_helper(a_list, left, right):
    if left < right:
        right_mark = partition(a_list, left, right)
        # 从分割点左右递归调用
        fast_sort_helper(a_list, left, right_mark - 1)
        fast_sort_helper(a_list, right_mark + 1, right)


def partition(a_list, left, right):
    middle_index = (left + right) // 2
    if (a_list[right] > a_list[middle_index] > a_list[left]) or \
            (a_list[left] > a_list[middle_index] > a_list[right]):
        a_list[middle_index], a_list[left] = a_list[left], a_list[middle_index]
    if (a_list[left] > a_list[right] > a_list[middle_index]) or \
            (a_list[middle_index] > a_list[right] > a_list[left]):
        a_list[left], a_list[right] = a_list[right], a_list[left]
    middle_value = a_list[left]
    left_mark = left + 1
    right_mark = right
    done = False
    while not done:
        # 左标往右走
        while left_mark <= right_mark and a_list[left_mark] <= middle_value:
            left_mark += 1
        # 右标往左
        while right_mark >= left_mark and a_list[right_mark] >= middle_value:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            # 交换左右数字
            a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]
    # 交换“中间”数与右标所对数，右标就是新的分割点
    a_list[left], a_list[right_mark] = a_list[right_mark], a_list[left]
    return right_mark


# 快速排序
def fast_sort(b_list: list):
    """
    列表快速排序，理论上最快的反而很慢。。。:
    原因在于timeit的重复次数，如果重复10次，那么后九次排序数组为已排好序
    如何修改成不是递归的形式
    :param b_list:
    :return:
    """
    fast_sort_helper(b_list, 0, len(b_list) - 1)
    # a_list.sort()


# 无递归快速排序
def fast_sort_nr(a_list: list):
    st = Stack()
    if len(a_list) > 1:
        st.push({'left': 0, 'right': len(a_list) - 1})
    while not st.is_empty():
        pt = st.pop()
        split_pos = partition(a_list, pt['left'], pt['right'])
        if pt['left'] < split_pos - 1:
            st.push({'left': pt['left'], 'right': split_pos - 1})
        if split_pos + 1 < pt['right']:
            st.push({'left': split_pos + 1, 'right': pt['right']})
    return a_list


def test_sort(repeat, number):
    merge_time = timeit.Timer(stmt='merge_sort(nums)',
                              setup="from __main__ import merge_sort;"
                                    "from __main__ import nums_origin;"
                                    "nums = nums_origin[:]")
    bubble_time = timeit.Timer(stmt='bubble_sort(nums)',
                               setup="from __main__ import bubble_sort;"
                                     "from __main__ import nums_origin;"
                                     "nums = nums_origin[:]")
    fast_time = timeit.Timer(stmt='fast_sort(nums)',
                             setup="from __main__ import fast_sort;"
                                   "from __main__ import nums_origin;"
                                   "nums = nums_origin[:]")
    fast_nr_time = timeit.Timer(stmt='fast_sort_nr(nums)',
                                setup="from __main__ import fast_sort_nr;"
                                      "from __main__ import nums_origin;"
                                      "nums = nums_origin[:]")
    insert_time = timeit.Timer(stmt='insert_sort(nums)',
                               setup="from __main__ import insert_sort;"
                                     "from __main__ import nums_origin;"
                                     "nums = nums_origin[:]")
    python_time = timeit.Timer(stmt='nums.sort()',
                               setup="from __main__ import nums_origin;"
                                     "nums = nums_origin[:]")
    print("| 排序方法 | 时间 |")
    print("| :-: | :-: |")
    print("| python time: |", sum(python_time.repeat(repeat, number)) / 3, '|')
    print("| bubble sort: |", sum(bubble_time.repeat(repeat, number)) / 3, '|')
    print("| insert sort: |", sum(insert_time.repeat(repeat, number)) / 3, '|')
    print("| merge sort: |", sum(merge_time.repeat(repeat, number)) / 3, '|')
    print("| fast nr sort: |", sum(fast_nr_time.repeat(repeat, number)) / 3, '|')
    print("| fast sort: |", sum(fast_time.repeat(repeat, number)) / 3, '|')


if __name__ == '__main__':
    nums_origin = [randint(1, 10000) for i in range(5000)]
    test_sort(3, 3)
