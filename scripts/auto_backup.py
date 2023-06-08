"""
配合Linux的Cron，自动打包备份远程指定目录的所有文件
功能:

1. 自动拉取文件
2. 自动打包
3. 自动保存最新的N份
"""
import itertools

# 斐波那契数列
def fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    for i in fib(1000):
        print(i, end=' ')

    # for i, j, k in itertools.product(*[range(5)] * 3):
    #     print(i, j, k)
