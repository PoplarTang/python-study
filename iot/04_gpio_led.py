import gpio
import os
import ohos

current = 0

gpio_num = 2
gpio.gpio_init(gpio_num)

func = gpio.query_func_value(gpio_num, 'gpio')

print("----------gpio:", func)

gpio.set_func(gpio_num, func)

gpio.set_dir(gpio_num, gpio.dir_out)

for i in range(10):
    if current == 0:
        current = 1
    else:
        current = 0

    gpio.set_output(gpio_num, current)

    cur_tick = os.get_tick()
    # os.sleep(1)
    ohos.usleep(1 * 1000 * 1000)

    end_tick = os.get_tick()
    print("os---------------i: {} gpio: {} current: {} tick: {}".format(i, gpio_num, current, end_tick))


gpio.gpio_deinit(gpio_num)