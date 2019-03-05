from _collections_abc import Iterable

class MyList:
    def __init__(self):
        self.items = list()

    def addItem(self, data):
        self.items.append(data)

    def __iter__(self):
        return MyIterator(self.items)

class MyIterator:

    def __init__(self, items):
        self.items = items
        self.current_index = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.current_index < len(self.items):
            data = self.items[self.current_index]
            self.current_index += 1
            return data
        else:
             raise StopIteration

if __name__ == '__main__':
    lst = MyList()
    lst.addItem("aa")
    lst.addItem("bb")
    lst.addItem("cc")

    print(isinstance(lst, Iterable))

    for i in lst:
        print(i)

