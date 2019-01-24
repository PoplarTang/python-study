class Dog:
    def __init__(self, name):
        self.type = "狗狗"
        self.name = name

    def eat(self):
        print("%s 在吃东西" % self.name)

    def __str__(self) -> str:
        return "哈哈哈, 我是" + self.name + super.__str__(self)


if __name__ == '__main__':
    print(Dog("狗子"))
    Dog("旺财").eat()
    Dog("来福").eat()
