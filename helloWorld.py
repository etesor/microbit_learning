from microbit import *
import random
import radio
import time

def showImage(string, delay):
    for letter in string:
        display.show(letter)
        sleep(delay)
    display.show(Image.HEART)
    sleep(delay)

str1 = "HELLO"
str2 = "WORLD"
def displayImages():
    if button_a.was_pressed():
        showImage(str1, 800)
    if button_b.was_pressed():
        showImage(str2, 800)
    display.clear()

def useAccelerometer():
    reading = accelerometer.get_x()
    if reading > 20:
        display.show(Image.ARROW_E)
    elif reading < -20:
        display.show(Image.ARROW_W)
    else: display.show("-")

def useTemperature():
    if button_a.was_pressed():
        display.scroll(temperature())

# Not fully sure this worked as expected on my Microbit version
def readLight():
    reading = display.read_light_level()
    display.scroll(reading)
    sleep(2000)

def useCompass():
    # Execute the calibration process automatically
    if button_a.was_pressed():
        display.scroll(str(compass.heading()))

def useRandom():
    if button_a.was_pressed():
        display.show(random.randint(0, 9))

def setupRadio():
    radio.config(group=23)
    radio.on()

duck = "duck"
hearth = "hearth"
def useRadio():
    message = radio.receive()
    if message and message is duck:
        display.show(Image.DUCK)
    elif message is hearth:
        display.show(Image.HEART)

    if button_a.was_pressed():
        display.clear()
        radio.send(duck)
    if button_b.was_pressed():
        display.clear()
        radio.send(hearth)


# Uncomment only if you want to test the radio features
# setupRadio()

while True:
    # Uncomment only ONE method to try it out.

    # displayImages()
    # useAccelerometer()
    # useTemperature()
    # readLight()
    # useCompass()
    # useRandom()
    # useRadio()

