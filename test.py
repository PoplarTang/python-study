from random import randint

def test():
    for i in range(10):
        print(randint(0,3))

def chengfabiao():
    """打印乘法口诀表"""
    for i in range(5):
        print(randint(0, 9))
    for i in range(9):
        for j in range(9):
            if j <= i:
                print("%d * %d = %d " % (j + 1, i + 1, (j + 1) * (i + 1)), end="\t")
        print()

def iter_del():
    list1 = [11,22,33,44,55]
    for i in range(len(list1) - 1, -1, -1):
        if list1[i] == 33:
            del list1[i]
            # list1.pop(i)
        else:
            print(list1[i])

    print(list1)

if __name__ == '__main__':
    # test()
    # chengfabiao()
    iter_del()
