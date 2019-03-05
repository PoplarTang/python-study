import threading

import time


class MyThread(threading.Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        for i in range(self.num):
            print("正在执行run函数 {} => {}".format(i, self.name))
            time.sleep(0.5)


if __name__ == '__main__':
    mt = MyThread(10)
    mt.start()
