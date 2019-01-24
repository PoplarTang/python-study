# 元组只能查询不能修改
# 支持index, count, for
# 元组是自动组包的默认类型
aa = 10, 20
print(aa)

a = 2
b = 3
b,a = a,b
print(a, b)


# 用于字符串格式化
info = "不错", "还行"
info = tuple(["不错", "还行"])

print("今天天气%s, 心情%s" % info)
