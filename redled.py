#!/usr/bin/python

from gpiozero import LED
from time import sleep


red = LED(17)

while True:
    red.on()
    sleep(1)
    red.off()
    sleep(0.1)
    red.on()
    sleep(1)
    red.off()
    sleep(0.1)
    red.on()
    sleep(1)
    red.off()
    sleep(0.1)
##---    

    red.on()
    sleep(2)
    red.off()    
    sleep(1)
    red.on()
    sleep(2)
    red.off()
    sleep(1)
    red.on()
    sleep(2)
    red.off()
## --
    sleep(1)
    red.on()
    sleep(1)
    red.off()
    sleep(0.1)
    red.on()
    sleep(1)
    red.off()
    sleep(0.1)    
    red.on()
    sleep(1)
    red.off()
    sleep(1.0)
