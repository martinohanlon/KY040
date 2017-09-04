# KY040 Python Module

> Martin O'Hanlon (martin@ohanlonweb.com)
>
> http://www.stuffaboutcode.com

A python module for reading the values from a KY040 rotary encoder module using a Raspberry Pi.

http://www.stuffaboutcode.com/2015/05/raspberry-pi-and-ky040-rotary-encoder.html

![KY040](ky040.jpg)

## Usage

``` python
# Define your pins
CLOCKPIN = 5
DATAPIN = 6
SWITCHPIN = 13

# Callback for rotary change
def rotaryChange(direction):
    print "turned - " + str(direction)

# Callback for switch button pressed
def switchPressed():
    print "button pressed"

# Create a KY040 and start it
ky040 = KY040(CLOCKPIN, DATAPIN, SWITCHPIN, rotaryChange, switchPressed)
ky040.start()
```


## Wiring

![Wiring](RaspberryPiKY040_bb.jpg)


## Version history
* 0.1 - Initial stable version
* 0.2 - Minor improvement

## License

This project is under [MIT](LICENSE) License.
