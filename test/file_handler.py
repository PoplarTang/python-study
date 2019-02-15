import re

def read_replace():
    with open("menu.txt", mode='r', encoding='UTF-8') as f, open("new.txt", "w+",encoding='UTF-8') as new_file:
        lines = f.readlines()
        for line in lines:
            # print("*"+line, end="")
            sub = re.sub(r"([』《\u4e00-\u9fa5]+)([^\n\u4e00-\u9fa5]*)$", r"\1", line, re.M | re.I)
            # sub = re.sub(r'([\u4e00-\u9fa5]+)([^\u4e00-\u9fa5]+)$', r'\1', line)
            print(sub, end="")
            new_file.write(sub)


sss = "12-1 什么是行列式  `* D1 @9 b# Y( Q+ C \n"
rrr = "14-6 实践scipy中的SVD分解) t  W0 B8 s& t5 Z! s. {% |"

def tst():
    sub = re.sub(r"([\u4e00-\u9fa5]+).*$", r"\1", rrr, re.M | re.I)
    print(sub)
    print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
    print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配
    search = re.search(r'([\u4e00-\u9fa5]+)([^\u4e00-\u9fa5]+)$', sss, re.M | re.I)
    print(search.group())
    print(search.group(1))
    print(search.group(2))


if __name__ == '__main__':
    read_replace()
    # tst()

