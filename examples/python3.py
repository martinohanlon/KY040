from time import sleep
import RPi.GPIO as GPIO
from ky040.KY040 import KY040


CLOCKPIN = 5
DATAPIN = 6
SWITCHPIN = 13


def rotaryChange(direction):
    print("turned - " + str(direction))


def switchPressed():
    print("button pressed")


GPIO.setmode(GPIO.BCM)

ky040 = KY040(CLOCKPIN, DATAPIN, SWITCHPIN, rotaryChange, switchPressed)

ky040.start()

try:
    while True:
        sleep(0.1)
finally:
    ky040.stop()
    GPIO.cleanup()
