import multiprocessing
import time

def copy_work():
    print("拷贝中 ", multiprocessing.current_process().pid)
    time.sleep(0.3)

if __name__ == '__main__':

    # process = multiprocessing.Process(target=copy_work)
    # process.start()

    pool = multiprocessing.Pool(3)
    for i in range(10):
        # 同步
        # pool.apply(copy_work)

        # 异步
        pool.apply_async(copy_work)

    pool.close()
    # 如果使用async异步执行任务，则主线程不再等待子线程，直接全部退出
    pool.join()





