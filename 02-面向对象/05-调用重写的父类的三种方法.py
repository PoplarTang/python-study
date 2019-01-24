class Dog:
    def eat(self):
        print("吃饭")


class XTQ(Dog):
    def eat(self):
        # Dog.eat(self)
        # super(XTQ, self).eat()
        super().eat()
        print("吃蟠桃")


xtq = XTQ()
xtq.eat()
