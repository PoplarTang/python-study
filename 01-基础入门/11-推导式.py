# 列表推导式
#  [0,2...9]
list1 = [i for i in range(10)]

list1 = [i for i in range(10) if i % 2 == 0]

print(list1)

# 字典推导式
dict1 = {str(i): i ** 2 for i in range(10)}
print(dict1)

dict2 = {"name":"zhangsan", "age": 12}
dict2 = {val:key for key,val in dict2.items()}
print(dict2)

# 无序集合推导式
list2 = ["xiaoming", "zhangyi", "xiaoming", "liulian", "xiaowang"]
list2 = [name for name in list2 if name.startswith("x")]
list2 = {name for name in list2 if name.startswith("x")}
print(list2)
