import gpio
import os

led = 2
button = 14

led_on = False


def button_callback(arg):
    cur_tick = os.get_tick()

    if cur_tick - arg[0] < 30:
        return

    global led_on
    if led_on:
        gpio.set_output(led, 0)
        led_on = False
        print('LED is OFF!')
    else:
        gpio.set_output(led, 1)
        led_on = True
        print('LED is ON!')

    arg[0] = cur_tick


gpio.gpio_init(led)
gpio.gpio_init(button)

func = gpio.query_func_value(led, 'gpio')
gpio.set_func(led, func)
gpio.set_dir(led, gpio.dir_out)
gpio.set_output(led, 0)

func = gpio.query_func_value(button, 'gpio')
gpio.set_func(button, func)
gpio.set_dir(button, gpio.dir_in)

pull_up = gpio.query_pull_value('up')

print("pull_up-----------------------: ", pull_up)
gpio.set_pull(button, pull_up)
gpio.set_isr_mode(button, gpio.fall_low)
gpio.register_isr_func(button, button_callback, [os.get_tick()])
print("waiting for click-----------------------: ", os.get_tick())

# while True:
#     os.sleep(1)
# gpio.gpio_deinit(led)
# gpio.gpio_deinit(button)
