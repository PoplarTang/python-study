class CustomException(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


while True:
    try:
        num = input("请输入手机号码:")
        if len(num) != 11:
            raise CustomException("请输入11位手机号")
        if not num.isdecimal():
            raise CustomException("请使用纯数字")
    except Exception as err:
        print(err)
    else:
        print("验证成功 %s" % num)
        break;
