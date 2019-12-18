"""
    leeCode第38题，报数，第二个数是第一个数的读法，例如第一个数1，第二个数就是11，读作“一个一”，
    第三个数就是21，读作两个一，第四个数1211，读作一个二一个一，以此类推
"""


def count_and_say(n: int) -> str:

    def next_pair(num: int, say: str):
        # 根据指定的数字n和他对应的数字字符串，获取字符串的读法作为第n+1个字符串
        # 返回n+1和字符串
        try:
            count = 0
            start_char = ""
            result = ""
            char = ""
            for char in say:
                if start_char == "":
                    count = 1
                    start_char = char
                else:
                    if char == start_char:
                        count = count + 1
                    else:
                        result = result + str(count) + start_char
                        count = 1
                        start_char = char
            if start_char != "":
                result = result + str(count) + char
            return num + 1, result
        except StopIteration:
            return 0, "error"

    p = (1, '1')
    for i in range(n):
        print(p)
        p = next_pair(*p)
    return p[1]


if __name__ == '__main__':
    count_and_say(3)
