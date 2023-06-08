# 语法糖：让你开心的语法
import functools
import time


# 装饰器
def timmer(func):
    # 定义一个新函数, 并且把原函数的参数传递过来
    # 加上wraps的目的是为了把原函数的属性也传递过来（如__name__）
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        print("cost:", stop - start)
        return res

    return wrapper


# 在被装饰对象正上方的单独一行写@装饰器名字
@timmer  # index=timmer(index)
def index(x, y, z):
    time.sleep(3)
    print('index %s %s %s' % (x, y, z))

@timmer  # home=timmer(ome)
def home(name):
    time.sleep(2)
    print('welcome %s to home page' % name)


print("index function name:", index.__name__)
index(x=1, y=2, z=3)

print("home function name:", index.__name__)
home('egon')
