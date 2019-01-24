# 可变参数和默认参数
def func_sum(*args, is_print=False):
    """可变参数和默认参数混合时, 默认参数应该放在可变参数后"""
    sum = 0
    for num in args:
        sum += num
    if is_print:
        print(sum)


# 关键字参数
def func(a, b, *args, defaultArg=False, **kwargs):
    """
    不同类型参数的排放方式
    :param a:           一般参数
    :param b:           一般参数
    :param args:        可变参数, 在形参前加*是对参数进行组包
    :param defaultArg:  默认参数
    :param kwargs:      字典类型的可变参数
    :return:
    """
    print(a, b)
    print(args)
    print(kwargs)
    print(defaultArg)




# 在实参前加 *
def fun1(a, b, c):
    print(a)
    print(b)
    print(c)


def split():
    print("-" * 20)


if __name__ == '__main__':
    func_sum(1, 2, 3, is_print=True)
    split()
    func(1, 2, 3, 4, defaultArg=True, m=5, n=6)
    split()
    tuple1 = (1, 2, 3)
    fun1(*tuple1) # 元组的拆包
    split()
    dict = {"a":3, "b":4, "c":5}
    fun1(**dict) # 字典的拆包

