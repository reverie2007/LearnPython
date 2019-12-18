import sqlite3


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            return "%f;%f" % (self.x, self.y)


class Line:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def adapt_line(line):
    return "%f:%f" % (line.x, line.y)


con = sqlite3.connect("test.db")
cur = con.cursor()
cur.execute("create table test(p)")

p = Point(4.0, -3.2)
cur.execute("insert into test(p) values(?)", (p,))
cur.execute("select ? from test", (p,))
print(cur.fetchone())

l = Line(2, 3)
l2 = Line(3, 42)
l3 = Line(4,32)
cur.execute("create table line(l, l2)")
sqlite3.register_adapter(Line, adapt_line)
cur.execute("insert into line(l, l2) values(?,?)", (l, l,))
cur.execute("select ? from line", ('line.l',))
print(cur.fetchone())
cur.execute("select ? from line", (l3,))
print(cur.fetchone())


con.close()
