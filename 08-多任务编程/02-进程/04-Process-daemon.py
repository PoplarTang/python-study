import multiprocessing
import time

def sub_process():
    for i in range(10):
        print("子进程运行中：", i)
        time.sleep(0.5)

if __name__ == '__main__':
    p1 = multiprocessing.Process(group=None, target=sub_process, name="p1")
    # p1.daemon = True
    p1.start()

    time.sleep(2)
    print("main over!")
    p1.terminate()
    exit()
