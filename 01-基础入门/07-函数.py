from random import randint

def test(r):
    """
    函数的注释
    :param r: 随机数个数
    :return: 随机数之和
    """
    result = 0
    for i in range(r):
        val = randint(0, 3)
        print(val)
        result += val
    return result

a = 10
def func():
    global a #声明a是个全局变量
    a = 2
    print(a)

def func_even_num(num):
    """求奇偶数"""
    if num % 2 == 0:
        return "偶数"
    else:
        return "奇数"

if __name__ == '__main__':
    test()
    # chengfabiao()
