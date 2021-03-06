#!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
from time import sleep
from random import randint

# this example uses a single shift register with normal 2-pin LED's

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

data_pin  = "P9_23"
latch_pin = "P9_25"
clock_pin = "P9_27"

GPIO.setup(data_pin, GPIO.OUT)
GPIO.setup(clock_pin, GPIO.OUT)
GPIO.setup(latch_pin, GPIO.OUT)

def delay(millis):
    millis_to_seconds = float(millis)/1000
    return sleep(millis_to_seconds)

while True:
    new_data = randint(0, 1)
    if new_data == 1:
        GPIO.output(data_pin, GPIO.HIGH)
        GPIO.output(clock_pin, GPIO.HIGH)
        GPIO.output(clock_pin, GPIO.LOW)
        GPIO.output(data_pin, GPIO.LOW)
    if new_data == 0:
        GPIO.output(clock_pin, GPIO.HIGH)
        GPIO.output(clock_pin, GPIO.LOW)
    GPIO.output(latch_pin, GPIO.HIGH)
    GPIO.output(latch_pin, GPIO.LOW)
    delay(400)
