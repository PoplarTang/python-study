class Dog:
    type = "狗"

    def eat(self):
        print(self.type + "吃饭")


def test_dog():
    dog1 = Dog()
    print(id(Dog.type))
    print(id(dog1.type))
    print("-" * 30)
    Dog.type = "gougou"
    print(dog1.type)
    print(id(dog1.type))
    print(id(Dog.type))
    print("-" * 30)
    dog1.eat()

class Cat:
    __type = "猫猫"

    @staticmethod
    def fly():
        print("让我飞一会儿")

    @classmethod
    def set_type(cls, type):
        cls.__type = type
        # 等同于 Cat.__type = type

    @classmethod
    def get_type(cls):
        return cls.__type

if __name__ == '__main__':
    # test_dog()
    print(Cat.get_type())
    Cat.set_type("miao")
    # 类和实例对象都可以调用类方法
    print(Cat.get_type())
    print(Cat().get_type())
    Cat.fly()

