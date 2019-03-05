def fibonacci(n):
    a = 1
    b = 1

    current_index = 0

    while current_index < n:
        result = a

        a, b = b, a + b

        current_index += 1
        
        yield  result
        return "huohuo"


if __name__ == '__main__':
    f = fibonacci(10)
    # for i in f:
    #     print(i)
    print(next(f)) # 第一次停到yield，没走到return

    try:
        print(next(f))
    except StopIteration as err:
        print("err: " + err.value)
