"""
    知乎帖子复制下来分割程序
"""


def read_zhihu():
    f = open('example.log', 'r', encoding='utf-8')
    reply_str = f.read()
    sp = reply_str.split(sep="收藏\n​感谢")
    print(len(sp))
    print(sp[380])


if __name__ == '__main__':
    read_zhihu()
