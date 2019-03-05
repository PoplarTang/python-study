import threading
import time

num = 0

def work1():
    global num

    for i in range(10):
        num += 1

    print("work1: ", num)


def work2():
    print("work2: ", num)


if __name__ == '__main__':
    threading.Thread(target=work1).start()
    threading.Thread(target=work2).start()

    while len(threading.enumerate()) != 1:
        time.sleep(1)

    print("num: ", num)
