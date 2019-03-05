from time import ctime, sleep
import threading
""""
获取当前线程名称/id
获取活动的线程数量
线程执行顺序
"""
def sing():
    for i in range(3):
        print("singing...{}, thread: {}".format(i,threading.current_thread()))
        sleep(i)

def dance():
    for i in range(3):
        print("dancing...{}, thread: {}".format(i,threading.current_thread()))
        sleep(i)

if __name__ == '__main__':
    print("start".center(15, "-"), ctime())

    print(threading.current_thread())

    t1 = threading.Thread(target=sing)
    t1.start()

    t2 = threading.Thread(target=dance)
    t2.start()

    while True:
        length = len(threading.enumerate())
        print("活跃线程数：", length)
        if length <= 1:
            break

        sleep(0.3)


    sleep(3)
    print("end".center(15, "-"), ctime())
