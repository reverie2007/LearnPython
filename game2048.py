#! /usr/bin/env python3
import pygame
import sys
import pygame.locals



'''
    2048game

'''



win = window()
#win.root.mainloop()

row = [0,0,4,0]
print(row)


def move_row(row):
    '''
    挪动一个一位数组内的方块至不能动为止，合并产生的方块不能再次合并
    负数表示刚合并产生的方块
    :param row:长度为4的一维数组
    :return:合并的步骤
    '''
    steps = []
    steps.append(row[:])
    move = True
    while move:
        move = False
        for i in range(1,4):
            if row[i] > 0:
                if row[i] == row[i - 1]:
                    row[i - 1],row[i] = row[i] * 2 * (-1),0
                    move = True
                elif row[i - 1] == 0:
                    row[i - 1],row[i] = row[i],0
                    move = True
                #else:
                #    pass
        if move:
            steps.append(row[:])
    return steps

steps = move_row(row)
print(steps)