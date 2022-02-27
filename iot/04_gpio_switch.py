import ohos
from genki import switch

if __name__ == '__main__':

    print("-----------init complete!")

    for i in range(5):
        switch.set_angle(i * 45)
        ohos.sleep(0.5)

    for i in range(4, -1, -1):
        switch.set_angle(i * 45)
        ohos.sleep(0.5)
