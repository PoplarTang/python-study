import gpio
import ohos

GPIO_PIN_LED = 2
GPIO_PIN_SERVO = 13
ONE_CYCLE_TIME = 20000

FREQUENCY_PWM_CONTROL = 50  # 50hz 每秒50个周期
pre_angle = -1


def init_gpio(gpio_num):
    gpio.gpio_init(gpio_num)
    func = gpio.query_func_value(gpio_num, 'gpio')
    print("gpio->{} func:{}".format(gpio_num, func))
    gpio.set_func(gpio_num, func)
    gpio.set_dir(gpio_num, gpio.dir_out)


def set_angle(angle_degrees):
    gpio.set_output(GPIO_PIN_LED, 1 if angle_degrees <= 90 else 0)

    high_time = 500 + angle_degrees * (2500 - 500) / 180.0
    print("1----------angle:{} time:{}".format(angle_degrees, high_time))

    global pre_angle
    angle_diff = 180
    if pre_angle != -1:
        angle_diff = abs(angle_degrees - pre_angle)

    pre_angle = angle_degrees

    fraq_count = 10 + int(FREQUENCY_PWM_CONTROL * angle_diff / 180.0)

    for i in range(fraq_count):
        gpio.set_output(GPIO_PIN_SERVO, 1)
        ohos.usleep(int(high_time))
        # ohos.sleep(high_time * 0.001 * 0.001)
        gpio.set_output(GPIO_PIN_SERVO, 0)
        ohos.usleep(int(ONE_CYCLE_TIME - high_time))
        # ohos.sleep(0.02 - high_time * 0.001 * 0.001)
    print("2----------angle:{} time:{} fraq_count:{}".format(angle_degrees, high_time, fraq_count))


def set_angle2(angle_degrees):
    gpio.set_output(GPIO_PIN_LED, 1 if angle_degrees <= 90 else 0)

    high_time = 500 + angle_degrees * (2500 - 500) / 180.0
    print("1----------angle:{} time:{}".format(angle_degrees, high_time))

    for i in range(50):
        gpio.set_output(GPIO_PIN_SERVO, 1)
        ohos.usleep(int(high_time))
        # ohos.sleep(high_time * 0.001 * 0.001)
        gpio.set_output(GPIO_PIN_SERVO, 0)
        ohos.usleep(int(ONE_CYCLE_TIME - high_time))
        # ohos.sleep(0.02 - high_time * 0.001 * 0.001)
    print("2----------angle:{} time:{}".format(angle_degrees, high_time))


if __name__ == '__main__':
    init_gpio(GPIO_PIN_LED)  # LED
    init_gpio(GPIO_PIN_SERVO)  # Servo (Torque)

    print("-----------init complete!")

    # set_angle(90)
    # ohos.sleep(0.5)
    #
    # set_angle(0)
    # ohos.sleep(0.5)
    #
    # set_angle(180)
    # ohos.sleep(0.5)

    for i in range(7):
        set_angle(i * 30)
        ohos.sleep(0.5)

    for i in range(6, -1, -1):
        set_angle(i * 30)
        ohos.usleep(int(0.5 * 1000 * 1000))

    gpio.gpio_deinit(GPIO_PIN_LED)
    gpio.gpio_deinit(GPIO_PIN_SERVO)
