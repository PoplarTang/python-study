import multiprocessing
import time
import sys

def write_queue(queue):
    for i in range(5):
        queue.put(i)
        print("正在写入：",i)
        time.sleep(0.5)

def read_queue(queue):
    while True:
        try:
            r = queue.get(True, 2)
            print("queue: " , r)
        except Exception as err:
            # print("队列超过2秒没数据，退出", sys.exc_info()[0])
            print("队列超过2秒没数据，退出", err)
            break

if __name__ == '__main__':
    queue = multiprocessing.Queue(3)

    p1 = multiprocessing.Process(target=write_queue, args=(queue,))
    p1.start()

    p2 = multiprocessing.Process(target=read_queue, args=(queue,))
    p2.start()

