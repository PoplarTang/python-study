from genki import led
import ohos
import pwm
import gpio


def led_pwm():
    for k in range(5):
        print("ohos-----------led_pwm: ", k)
        for i in range(30):
            led.pwm_start(i, 20000)  # >2441hz
            ohos.sleep(0.02)
            # os.usleep(int(20 * 1000))
        for i in range(30, -1, -1):
            led.pwm_start(i, 20000)  # >2441hz
            ohos.sleep(0.02)
            # os.usleep(int(20 * 1000))

    led.pwm_stop()


gpio_led = 2  # GPIO_11 连接了一个 LED 灯


def gpio_led_pwm():
    # 'gpio' 指基本输入输出功能
    gpio.gpio_init(gpio_led)  # 初始化系统 GPIO 环境

    func = gpio.query_func_value(gpio_led, 'pwm')
    gpio.set_func(gpio_led, func)  # 设置 GPIO_2 为pwm
    gpio.set_dir(gpio_led, gpio.dir_out)  # 设置 GPIO_2 作为输出使用

    pwm_num = gpio.query_pwm_value(gpio_led)
    print("--------pwm_num:", pwm_num)
    pwm.pwm_init(pwm_num)  # pwm初始化

    for k in range(5):
        print('start =======================> ', k)
        for i in range(0, 30):
            res = pwm.start(pwm_num, i, 20000)  # res启动结果状态。0为成功。其他为失败。
            ohos.usleep(50 * 1000)  # 休眠 0.05 秒

        for i in range(30, -1, -1):
            pwm.start(pwm_num, i, 20000)
            ohos.usleep(50 * 1000)  # 休眠 0.05 秒

        print('stop')

    pwm.pwm_deinit(pwm_num)
    gpio.gpio_deinit(gpio_led)


if __name__ == '__main__':
    led_pwm()
    # gpio_led_pwm()
