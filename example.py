import Adafruit_BBIO.GPIO as GPIO
from shiftr_74HC595 import ShiftRegister
from time import sleep

# SER   = Data
# RCLK  = Latch
# SRCLK = Clock
# SRCLR = Clear keep high
# OE    = Blank keep low

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
