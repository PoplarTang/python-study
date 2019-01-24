class Dog:
    def __init__(self):
        self.__age = None

    def eat(self):
        print("吃饭")

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


dog = Dog()
print(dog.get_age())
dog.set_age(12)
print(dog.get_age())
