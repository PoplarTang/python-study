import time
import threading

def daemon_work():

    for i in range(10):
        print("daemon_work正在执行中...", i)
        time.sleep(0.5)

if __name__ == '__main__':

    t1 = threading.Thread(target=daemon_work)
    t1.setDaemon(True)
    t1.start()

    time.sleep(2)
    print("Main end!")

    exit()

