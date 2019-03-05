from time import ctime, sleep
import threading
""""
线程参数
"""
def sing(a,b,c):
    print("sing参数：a={},b={},c={}".format(a,b,c))

    for i in range(3):
        print("singing...{}".format(i))
        sleep(i)

if __name__ == '__main__':
    print("start".center(15, "-"), ctime())

    print(threading.current_thread())

    # t1 = threading.Thread(target=sing, args=(11,22,33))
    # t1 = threading.Thread(target=sing, kwargs={"a": 111, "b": "222", "c":33.3})
    t1 = threading.Thread(target=sing, args=(11,), kwargs={"b":22, "c":33})
    t1.start()

    sleep(3)
    print("end".center(15, "-"), ctime())
