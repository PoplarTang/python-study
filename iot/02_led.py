from genki import led
import ohos
import os


def led_light():
    # while True:
    for i in range(12):
        led.toggle()
        print("net---ohos---led:{} i:{}".format(led.state(), i))
        # print("serial---ohos---led:{} i:{}".format(led.state(), i))
        # os.usleep(int(0.5 * 1000 * 1000)) # usleep 不阻塞
        ohos.usleep(int(0.5 * 1000 * 1000))  # hi_udelay 阻塞


led_light()
