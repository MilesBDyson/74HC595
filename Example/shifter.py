#!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
from time import sleep
from random import randint

# SER   = Data
# RCLK  = Latch
# SRCLK = Clock
# SRCLR = Clear keep high
# OE    = Blank keep low

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
    print new_data
    delay(400)
