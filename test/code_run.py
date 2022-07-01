def fun_test(a: int, b):
    print(type(a))
    print(type(b))


def add(a, b):
    return a + b


class Person:

    def __init__(self):
        self._name = "abc"
        self.__age = 123

    def _say_hi(self):
        print(self._name, "hi")

    def __say_hello(self):
        print(self._name, "hello")


if __name__ == '__main__':

    person = Person()
    print(person._name)
    # print(person.__age)
    person._say_hi()
    # person.__say_hello()
