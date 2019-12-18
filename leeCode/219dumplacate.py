"""
    重复元素
"""


def duplicate():
    nums = [1, 0, 1, 1]
    k = 1
    l_list = len(nums)
    print(l_list)
    if k >= l_list - 1:
        nums_set = set(nums)
        l_set = len(nums_set)
        return l_list != l_set  # 不相等说明有重复
    else:
        for i in range(l_list - k):
            print(nums[i:i + k + 1])
            l_set = len(set(nums[i:i + k + 1]))
            if l_set <= k:
                return True
        return False


if __name__ == '__main__':
    duplicate()
