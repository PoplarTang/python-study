# encoding=utf-8

def pwdInput():
    content = input("请输入密码:")
    print(type(content))
    print(int(content) * 2)


def moneyCalc():
    price = input("请输入单价:")
    count = input("请输入个数:")
    price = float(price)
    count = int(count)
    money = price * count
    print(money)


if __name__ == "__main__":
    moneyCalc()

