import ohos
from genki import switch

if __name__ == '__main__':

    print("-----------init complete!")

    # 0 -> 135
    for i in range(4):
        switch.set_angle(i * 45)
        ohos.sleep(0.5)

    # 180 -> 0
    for i in range(4, -1, -1):
        switch.set_angle(i * 45)
        ohos.sleep(0.5)

    switch.set_angle(90)
