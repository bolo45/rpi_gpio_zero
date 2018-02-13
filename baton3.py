#!/usr/bin/python

from gpiozero import Button
from signal import pause

global licznik
licznik = 0  


def say_hello():
    global licznik
    licznik = licznik + 1
    print("Hello!")
    print(licznik)

button = Button(2)

button.when_pressed = say_hello

pause()
