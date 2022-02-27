import gpio
import os
from genki import switch

button = 14

state_on = False


def button_callback(arg):
    cur_tick = os.get_tick()

    if cur_tick - arg[0] < 30:
        return

    global state_on
    if state_on:
        switch.open()
        print('switch open!')
    else:
        switch.close()
        print('switch close!')

    state_on = not state_on

    arg[0] = cur_tick


gpio.gpio_init(button)

func = gpio.query_func_value(button, 'gpio')
gpio.set_func(button, func)
gpio.set_dir(button, gpio.dir_in)

pull_up = gpio.query_pull_value('up')

print("pull_up-----------------------: ", pull_up)
gpio.set_pull(button, pull_up)
gpio.set_isr_mode(button, gpio.fall_low)
gpio.register_isr_func(button, button_callback, [os.get_tick()])

print("waiting for click--------------------!")

