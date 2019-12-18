"""
    使用@propety装饰后的属性究竟是什么东西
    属性装饰器如何实现的？

"""


class Student(object):
    _score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("Score must be int!")
        else:
            self._score = value


if __name__ == '__main__':
    stu = Student()
    print(type(stu))
    print(type(stu.score))
    stu.score = 80
    print(stu.score)
    print("score type:", Student.score)
