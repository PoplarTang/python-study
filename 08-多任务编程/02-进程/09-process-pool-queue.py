import multiprocessing
import time

def write_process(queue):
    for i in range(10):

        if queue.full():
            print("队列已满！")
            break

        queue.put(i)
        print("正在写入：",i)
        time.sleep(0.5)


def read_process(queue):
    while True:
        if queue.empty():
            print("队列已空！")
            break

        result = queue.get()
        print("正在获取：",result)


if __name__ == '__main__':
    pool = multiprocessing.Pool(2)

    queue = multiprocessing.Manager().Queue(3)

    result = pool.apply_async(write_process, (queue,))
    result.wait()

    pool.apply_async(read_process, (queue,))

    pool.close()
    pool.join()

    # result = pool.apply(write_process, (queue,))
    # pool.apply(read_process, (queue,))
    # pool.close()

