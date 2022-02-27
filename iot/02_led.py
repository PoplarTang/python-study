from genki import led
import ohos
import os


def led_light():
    # while True:
    for i in range(20):
        led.toggle()
        # print("net---os---led:{} i:{}".format(led.state(), i))
        print("serial---os---led:{} i:{}".format(led.state(), i))
        # os.usleep(int(0.5 * 1000 * 1000)) # usleep 不阻塞
        ohos.usleep(int(0.5 * 1000 * 1000)) # hi_udelay 阻塞


def led_pwm():
    for i in range(10):
        print("------led: ", i)
        for i in range(50):
            led.pwm_start(i, 20000)
            # ohos.sleep(0.02)
            os.usleep(int(20 * 1000))
        for i in range(50, -1, -1):
            led.pwm_start(i, 20000)
            # ohos.sleep(0.02)
            os.usleep(int(20 * 1000))


if __name__ == '__main__':
    led_light()
    # led_pwm()
