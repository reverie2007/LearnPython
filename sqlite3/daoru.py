import jiekou2
import jiekou

print("%s have a num:" % __name__, jiekou.num)
print("%s have a num:" % __name__, jiekou2.num)

print(len(dir(__builtins__)))
try:
    None[0]
except TypeError as e:
    print("type error!", e)
x = 'sfefjdisjfkdsj'
print(hash(x))
print(hash(123456789101183) == 101718800)
print(hash(101718800))
dir()
