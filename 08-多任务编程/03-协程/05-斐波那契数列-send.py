def fibonacci(n):
    a = 1
    b = 1

    current_index = 0

    while current_index < n:
        result = a

        a, b = b, a + b

        current_index += 1

        params = yield result
        print("send-------", params)


if __name__ == '__main__':
    f = fibonacci(10)

    # 首次使用send执行生成器的时候传入的参数必须是None，下次启动生成器的时候可以加上参数
    print(f.send(None)) # 或使用next 唤醒生成器
    print(f.send(123))
    print(f.send("abc"))



