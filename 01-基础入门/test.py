from timeit import Timer
import time

print(Timer.__doc__)

print(Timer.timeit.__doc__)

# print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# print(Timer('a,b = b,a', 'a=1; b=2').timeit())

print(time.process_time())
print(time.time())
print('-------------------------------')
start = time.time()
arr2 = [i for i in range(1000000) if i % 2 == 0]

print("len1: {0:d} duration: {1:f}".format(len(arr2), time.time() - start))

start = time.time()
arr3 = list(filter(lambda x: x % 2 == 0, range(1000000)))
print("len2: {0:d} duration: {1:f}".format(len(arr3), time.time() - start))

# 每秒多少帧 60dps
# 1 / 最近10帧的平均间隔

print(time.process_time())
print(time.time())
arr = [1, 2, 3, 4]
print(round(sum(arr) / len(arr)))
print(round(2.8))

print("dps: {0:3d}".format(23))
print("dps: {0:3d}".format(123))

# print(Timer('[i for i in range(100) if i % 2 == 0]','').timeit())
# print(Timer('list(filter(lambda x: x % 2 == 0, range(100)))','').timeit())
