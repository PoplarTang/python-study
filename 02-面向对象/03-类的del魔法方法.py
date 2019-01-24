class Dog:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("%s 要被回收销毁了" % self.name)

    def say(self):
        print(self.name + ": 旺旺")


dog = Dog("旺财")
dog.say()
print("1" * 30)

Dog("来福").say()
print("2" * 30)

def main():
    dd = Dog("狗狗")

main()
print("3" * 30)
