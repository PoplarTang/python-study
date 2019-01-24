list = [4, 5, 11, 2, 3, "6", 67]

# 添加
list.extend("abc")
list.extend([11, 22])
list.append("haha")
list.insert(2, "insert")

# 删除
list.remove("6")
print(list)
pop = list.pop(1)  # 默认pop最后一个元素
print(list, pop)
# list.clear()

# 查询
print(list.index(11, 0, 3))
print(list.count(11))
print('b' in list)

# 排序
list2 = [4, 6, 1, 2, 56, 12, "7"]
list2.sort(key=int)
print(list2)

list.sort(key=str)
print(list)
list.reverse()
print(list)

# for str in "abc123":
#     print(str)

list3 = [1,2,3]
print(list3 * 3)


# 同时循环两个或更多的序列，可以使用 zip() 整体打包:

questions=['name','quest','favorite color']
answers=['lancelot','the holy grail','blue']
for q, a in zip(questions,answers):
    print('What is your {0}?  It is {1}.'.format(q,a))
# What is your name?  It is lancelot.
# What is your quest?  It is the holy grail.
# What is your favorite color?  It is blue.
