import multiprocessing
import time
import os

def work():
    print("os.getpid() ",os.getpid())
    print("os.getppid() ",os.getppid())
    print("work: ", multiprocessing.current_process())
    print("work: ",multiprocessing.current_process().pid)

    for i in range(10):
        print("work".ljust(10, '-'), i)
        time.sleep(0.5)

if __name__ == '__main__':
    print("main: ", multiprocessing.current_process())
    print("main: ", multiprocessing.current_process().pid)
    print("main: ", os.getpid())

    p1 = multiprocessing.Process(group=None, target=work)
    p1.start()

    for i in range(10):
        print("主进程".ljust(10, '-'), i)
        time.sleep(0.5)

