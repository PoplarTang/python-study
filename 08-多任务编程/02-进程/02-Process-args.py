import multiprocessing
import time
import os

num = 100

def work(arr):
    global num
    num += 1
    arr[0] = 666
    print("work".ljust(10, "-"), num)
    print("work".ljust(10, "-"), arr)

def work1(arr):
    time.sleep(2)
    print("work1".ljust(10, "-"), num)
    print("work1".ljust(10, "-"), arr)

if __name__ == '__main__':
    arr = [11, 22, 33]
    multiprocessing.Process(group=None, target=work, args=(arr,), name="MyProcess").start()
    multiprocessing.Process(group=None, target=work1, args=(arr,),name="MyProcess1").start()
