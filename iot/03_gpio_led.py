import gpio
import os

current = 0

gpio_num = 2
gpio.gpio_init(gpio_num)

func = gpio.query_func_value(gpio_num, 'gpio')

print("----------gpio:", func)

gpio.set_func(gpio_num, func)

gpio.set_dir(gpio_num, gpio.dir_out)

while True:
    if current == 0:
        current = 1
    else:
        current = 0

    gpio.set_output(gpio_num, current)

    cur_tick = os.get_tick()
    # os.sleep(2)
    os.usleep(1 * 1000 * 1000)

    end_tick = os.get_tick()
    print("---------------gpio: {} current: {} tick: {}".format(gpio_num, current, end_tick))


gpio.gpio_deinit(gpio_num)