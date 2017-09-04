#KY040 Python Class
#Martin O'Hanlon
#stuffaboutcode.com

import RPi.GPIO as GPIO


class KY040:

    CLOCKWISE = 0
    ANTICLOCKWISE = 1

    def __init__(self, clockPin, dataPin, switchPin=None, rotaryCallback=None, switchCallback=None, rotaryBouncetime=250, switchBouncetime=300):
        # persist values
        self.clockPin = clockPin
        self.dataPin = dataPin
        self.switchPin = switchPin
        self.rotaryCallback = rotaryCallback
        self.switchCallback = switchCallback
        self.rotaryBouncetime = rotaryBouncetime
        self.switchBouncetime = switchBouncetime

        #setup pins
        GPIO.setup(clockPin, GPIO.IN)
        GPIO.setup(dataPin, GPIO.IN)

        if None != self.switchPin:
            GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def start(self):
        GPIO.add_event_detect(self.clockPin, GPIO.FALLING, callback=self._clockCallback, bouncetime=self.rotaryBouncetime)

        if None != self.switchPin:
            GPIO.add_event_detect(self.switchPin, GPIO.FALLING, callback=self._switchCallback, bouncetime=self.switchBouncetime)

    def stop(self):
        GPIO.remove_event_detect(self.clockPin)

        if None != self.switchPin:
            GPIO.remove_event_detect(self.switchPin)

    def _clockCallback(self, pin):
        if GPIO.input(self.clockPin) == 0:
            data = GPIO.input(self.dataPin)
            if data == 1:
                self.rotaryCallback(self.ANTICLOCKWISE)
            else:
                self.rotaryCallback(self.CLOCKWISE)

    def _switchCallback(self, pin):
        if None == self.switchPin:
            return

        if GPIO.input(self.switchPin) == 0:
            self.switchCallback()
