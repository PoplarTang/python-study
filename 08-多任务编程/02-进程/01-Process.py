import multiprocessing
import time

def work():
    for i in range(10):
        print("work".ljust(10, '-'), i)
        time.sleep(0.5)

if __name__ == '__main__':
    p1 = multiprocessing.Process(group=None, target=work)
    p1.start()

    for i in range(10):
        print("主进程".ljust(10, '-'), i)
        time.sleep(0.5)

