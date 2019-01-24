class Dog:
    def eat(self):
        print("吃青菜")


class God:
    def fly(self):
        print("飞起来~")

    def eat(self):
        print("吃蟠桃")


# class XTQ(God, Dog):
#     pass
class XTQ(God, Dog):
    def eat(self):
        # super(God, self).eat()  查找God下一级类的eat方法 (Dog的)
        # 继承关系复杂时, 通过直接指定父类名来调用指定父类的方法
        Dog.eat(self)


xtq = XTQ()
xtq.fly()
xtq.eat()
print(XTQ.__mro__)  # 查看继承链(元组)
