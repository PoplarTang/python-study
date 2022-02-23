from genki import led
import ohos


def led_light():
    while True:
        led.toggle()
        ohos.sleep(0.5)


def led_pwm():
    while True:
        for i in range(50):
            led.pwm_start(i, 20000)
            print("------led: ", led.state())
            ohos.sleep(0.02)
        for i in range(50, -1, -1):
            led.pwm_start(i, 20000)
            print("------led: ", led.state())
            ohos.sleep(0.02)


if __name__ == '__main__':
    led_pwm()
