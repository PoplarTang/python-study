# 使用方式一, 直接导入
import module
module.func()
print(module.count)
print(module.Dog)

# 方式二, 按需导入
# from module import func, count
# func()
# print(count)

# 方式三, 导入all
from module import *
func()
print(count)
# print(Dog)

import sys

# 打印可导入的模块路径
print(sys.path)
