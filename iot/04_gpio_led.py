import gpio
import os
import ohos

current = 0

gpio_num = 2
# 'gpio' 指基本输入输出功能
gpio.gpio_init(gpio_num)

# 查询指定引脚的对应功能索引
func = gpio.query_func_value(gpio_num, 'gpio')  # uart, spi, pwm, i2c

print("----------gpio:", func)
# 对指定引脚设置对应功能
gpio.set_func(gpio_num, func)

# 设置为输出方向
gpio.set_dir(gpio_num, gpio.dir_out)  # dir_in输入 dir_out输出

for i in range(10):
    if current == 0:
        current = 1
    else:
        current = 0

    gpio.set_output(gpio_num, current) # 0为低电压，1为高电压

    cur_tick = os.get_tick()
    # os.sleep(1)
    ohos.usleep(1 * 1000 * 1000)

    end_tick = os.get_tick()
    print("os---------------i: {} gpio: {} current: {} tick: {}".format(i, gpio_num, current, end_tick))

gpio.gpio_deinit(gpio_num)
