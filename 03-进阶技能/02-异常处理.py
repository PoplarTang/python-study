import sys
def readFile():
    while True:
        try:
            path = input("请输入文件路径:")
            with open(path, "r") as f:
                print(f.read())
        except:
            print("出现异常")


def inputNum():
    while True:
        try:
            num = input("请输入数字:")
            print(int(num))
            # print(1/0)
        except (ValueError,ZeroDivisionError) as err:
            print("Could not convert data to an integer -> {0}".format(err))
        except TypeError as err:
            print("TypeError -> {0}".format(err))
        except:
            print("Unexpected error:",sys.exc_info()[0])
            raise # 抛出
        else:
            print("没有任何异常的来到else这里了")
            break
        finally:
            print("finally!")


if __name__ == '__main__':
    # readFile()
    inputNum()

