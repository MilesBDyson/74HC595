import Adafruit_BBIO.GPIO as GPIO
from shiftr_74HC595 import ShiftRegister
from time import sleep

# Basic example using the shiftr_74HC595 library

'''
SER   = Data
RCLK  = Latch
SRCLK = Clock
SRCLR = Clear (keep high)
OE    = Blank (keep low)

       74HC595
       -------
 QB --|1    16|-- VCC
 QC --|2    15|-- QA
 QD --|3    14|-- SER
 QE --|4    13|-- OE
 QF --|5    12|-- RCLK
 QG --|6    11|-- SRCLK
 QH --|7    10|-- SRCLR
GND --|8     9|-- QH'           <--- DATA OUT to SER on next IC to daisy chain them
       -------
'''

data_pin  = "P9_23" #pin 14 on the 75HC595
latch_pin = "P9_25" #pin 12 on the 75HC595
clock_pin = "P9_27" #pin 11 on the 75HC595

shift_register = ShiftRegister(data_pin, latch_pin, clock_pin)

try:
    while 1:
        # Set all outputs
        shift_register.setOutputs([GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW])
        # Display
        shift_register.latch()
        sleep(0.1)
        shift_register.setOutputs([GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH])
        # Display
        shift_register.latch()
        sleep(0.1)

        # Set some output individually
        #shift_register.setOutput(0, GPIO.LOW)
        #shift_register.setOutput(5, GPIO.HIGH)
        #shift_register.latch()
        #sleep(1)
except KeyboardInterrupt:
    print "Ctrl-C - quit"

GPIO.cleanup()
