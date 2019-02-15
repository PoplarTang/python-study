from collections import deque

def 列表队列():
    """列表队列"""
    queue = deque(["Apple", "Banana", "Cat"])
    queue.append("Eva")
    queue.append("Haha")
    queue.popleft()
    print(queue)


def 花样列表推导式():
    # 列表转二维列表
    vec = [1, 2, 3]
    vec2 = [[x, x ** 2] for x in vec]
    print(vec2)

    vec3 = [5, 6, -7]
    vec4 = [x*y for x in vec for y in vec3]
    print(vec4)
    print([repr(round(355/113, i)) for i in range(1,7)])


def 列表嵌套():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    # 矩阵的转置
    change = [[row[i] for row in matrix] for i in range(4)]
    print(change)


if __name__ == '__main__':
    # 列表队列()
    花样列表推导式()
    # 列表嵌套()
