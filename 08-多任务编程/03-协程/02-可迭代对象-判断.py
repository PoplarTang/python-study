from _collections_abc import Iterable

print(isinstance((1,2), Iterable))
print(isinstance({"aa",2, 3.1}, Iterable))
print(isinstance({"a":1,"b":2}, Iterable))
print(isinstance("haha", Iterable))
