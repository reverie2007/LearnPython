"""
    example using Queue class
    打印序列模拟：某实验室有一台共享打印机，有实验人员10，每小时需打印2次，每次打印1-20页不等。打印机每分钟打印5页（质量好）
    或10页（草稿模式），应该如何设置打印质量来获得可接受的等待时间？
    解题思路：设计一次模拟，求出平均等待时间，改变参数看等待时间的变化
"""
from pythonds.basic.queue import Queue
import random


class Printer:
    def __init__(self, speed):
        self.print_speed = speed
        self.task = None
        self.time_remain = 0

    def start_next(self, task):
        self.task = task
        self.time_remain = task.pages * 60 / self.print_speed

    def tick(self):
        if self.task is not None:
            self.time_remain -= 1
            if self.time_remain <= 0:
                self.task = None

    def is_busy(self):
        return self.task is not None


class Task:
    def __init__(self, t, pages):
        self.start_time = t
        self.pages = pages

    def wait_time(self, current_time):
        return current_time - self.start_time


def print_task_simulation():
    speed = 20  # 打印速度，页/每分钟
    printer = Printer(speed)
    task_queue = Queue()

    current_time = 0
    wait_times = []
    while current_time < 3601:
        if random.randint(1, 180) == 100:
            task_queue.push(Task(current_time, random.randint(1, 20)))

        if not task_queue.is_empty() and not printer.is_busy():
            task = task_queue.pop()
            wait_times.append(task.wait_time(current_time))
            printer.start_next(task)

        printer.tick()
        current_time += 1

    average_time = sum(wait_times) / len(wait_times)
    print("Average waiting time is :", average_time, end=' ')
    print("Task left in queue:", task_queue.size())


def main():
    for i in range(10):
        print_task_simulation()


if __name__ == '__main__':
    main()
