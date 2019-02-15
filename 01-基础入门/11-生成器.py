"""
使用了yield的函数称为生成器generator
"""
import sys

def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)

print(type(f))
lst = list(f)
print(type(lst))
print(len(lst))
print(lst)

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
