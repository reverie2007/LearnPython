import _sqlite3
import sqlite3
import types

num = 11
print("%s have a num:" % __name__, num)
if __name__ == '__main__':
    print(dir(_sqlite3))
    print(dir(sqlite3))
    print(dir(types))
