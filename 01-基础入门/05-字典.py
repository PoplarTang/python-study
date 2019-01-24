import sys

dict = {"name": "姓名", "age": 12}
print(dict)

# 设置默认数值, 存在则不修改
dict.setdefault("from", "广东")
print(dict)

dict["sex"] = 1

pop = dict.pop("sex")
del dict["from"]

dict.update({"like": "computer", "phone":13511112222})

print(dict)

# 取数据, 不存在不报错, 返回None
print(dict.get("name"))
print(dict.get("haha"))

keys = dict.keys() # 视图对象, 支持for, in, 转换列表
list = list(keys)
print(sys.getsizeof(keys))
print(sys.getsizeof(list))

print("name" in keys)
for i, key in enumerate(keys):
    print(i, key)

print(type(dict.values()))
print(type(dict.items()))
for key, value in dict.items():
    print(key, value)

list1 = [1,3,4]

list_str = str(list1)
dict_str = str(dict)

print(list_str)
print(dict_str)
print("-" * 30)
# with eval(list_str) as list_data:
#     print(type(list_data), list_data)
print(eval(list_str))
print(type(eval(list_str)))

print(eval(dict_str))
print(type(eval(dict_str)))
