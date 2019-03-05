import time

def work1():
    num = 0
    while True:
        time.sleep(0.3)
        yield "work1-->{}".format(num)
        num += 1

def work2():
    num = 0
    while True:
        time.sleep(0.3)
        yield "work2-->{}".format(num)
        num += 1


if __name__ == '__main__':
    w1 = work1()
    w2 = work2()

    while True:
        print(next(w1))
        print(next(w2))
