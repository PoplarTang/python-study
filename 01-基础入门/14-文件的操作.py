def write():
    f = open("aaa.txt", "w")
    f.write("hello")
    f.close()


def write_auto_close():
    with open("aaa.txt", "w") as f:
        f.write("python")


def write_append():
    with open("aaa.txt", "a") as f:
        f.write("haha")


def read_file():
    with open("aaa.txt", "r") as f:
        return f.read()


if __name__ == '__main__':
    # write() #写数据
    # write_auto_close()
    # write_append()
    # print(read_file())
    filename = "aaa.txt"
    name, _, postfix = filename.rpartition(".")
    new_name = name + "[副本]." + postfix
    print(new_name)
