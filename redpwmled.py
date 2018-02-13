#!/usr/bin/python


from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)

while True:
    led.value = 0  # off
    sleep(1)
    led.value = 0.16  # half brightness
    sleep(1)
    led.value = 0.32  # full brightness
    sleep(1)
    led.value = 0.49  # off
    sleep(1)
    led.value = 0.66 # half brightness
    sleep(1)
    led.value = 1  # full brightness
    sleep(1)


