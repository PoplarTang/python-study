with open("bbb.txt", "w+") as f:
    print(f.tell()) # 查看当前光标定位
    f.write("hello")
    print(f.tell())
    """
    offset 表示字节偏移数 (whence为0时才能生效)
    whence 何处 0开头,1不变,2尾部
    """
    f.seek(2,0)     # 调整光标位置
    print(f.read())
