import board
import time
from digitalio import DigitalInOut, Direction, Pull
import neopixel

# create a neopixel object
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
pixels.brightness = 0.1
# create a color as a tuple value
ac_orange = 0xfc4600
ac_green = 0x61fc00
ac_blue = 0x002efc
ac_red = 0xff0000
ac_cyan = 0x00ffff
ac_purple = 0x9400D3
ac_pink = 0xFFB6C1
ac_yellow = 0xFFFF00
ac_darkyellow = 0xCC9900

ColorList = [
    ac_orange, ac_green, ac_blue, ac_red, ac_cyan, ac_purple, ac_pink, ac_yellow, ac_darkyellow
]

# declare a digitial input
button_a = DigitalInOut(board.BUTTON_A)
button_a.switch_to_input(pull=Pull.DOWN)
button_b = DigitalInOut(board.BUTTON_B)
button_b.switch_to_input(pull=Pull.DOWN)

# A variable to track the LED led state
led_state = 0

'''
Week 2 Code Challenge:
Write a program that uses two buttons on the circuit playground bluefruit as inputs

When you push button A the lights should light up with ONE color
When you button button B the lights should light up with a SECOND color
When you push both buttons the lights should light up with a THIRD color

Use if and elif to make this happen:
if condition 1:
    code to execute
elif condition 2:
    code to execute
elif condition 3:
    code to execute
else:
    default code to execute

'''

while True:
    # gather all input values from sensors
    # print the value of our button_a object
    button_a_read = button_a.value
    button_b_read = button_b.value

    print("button a read is:", button_a_read, "button b read is:", button_b_read);
    # No color(0)
    # A: One color(1)
    # B: One color(2)
    # A, B: third color(3)
    # set variables based on the value of your inputs
    if (button_a_read == True) and (button_b_read == True):
        led_state = 3
    elif button_a_read:
        led_state = 2
    elif button_b_read:
        led_state = 1
    else:
        led_state = 0
    # set outputs based on the value of my variables
    if led_state == 1:
        # turn the neopixels ac_orange
        for i in range(0, 9):
            pixels[i+1] = ColorList[i]
            time.sleep(0.2)
    elif led_state == 2:
        for i in range(0, 9):
            pixels[9-i] = ColorList[i]
            time.sleep(0.2)
    elif led_state == 3:
        pixels.fill(ac_yellow)
    else:
        pixels.fill(0)
        # turn the neopixels off

    time.sleep(0.2)
