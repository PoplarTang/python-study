def fibonacci(n):
    a = 1
    b = 1

    current_index = 0

    while current_index < n:
        result = a

        a, b = b, a + b

        current_index += 1

        yield  result



if __name__ == '__main__':
    f = fibonacci(10)
    for i in f:
        print(i)

    # print(next(f))
    # print(next(f))
