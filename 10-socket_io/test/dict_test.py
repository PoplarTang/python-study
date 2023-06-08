d = {
    'name': 'Tom',
    'age': 18,
}

d2 = {
    'name': 'Tony',
    "height": 180,
}

# 移除掉d2中哪些不属于d.keys()的键值对
d2 = {k: v for k, v in d2.items() if k in d.keys()}

d.update(d2)

print(d)
print(d2)