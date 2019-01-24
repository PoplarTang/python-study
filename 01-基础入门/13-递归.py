# 递归
def func(num):
    if num == 0:
        return 0
    return num + func(num - 1)


# 尾递归 (未做优化, 无法实现, 需要引用三方库)
def recursion(num):
    return tail_recursion(num, 0)


def tail_recursion(num, product):
    if num == 0:
        return product
    return tail_recursion(num - 1, product + num)


if __name__ == '__main__':
    print(func(997))
    print(recursion(996))
