from _collections_abc import Iterator

data_list = [1,2,3,4,5]

list_iter = iter(data_list)

print(list_iter)
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))


print(isinstance([], Iterator))
print(isinstance(iter([]), Iterator))
print(isinstance(iter("abc"), Iterator))
