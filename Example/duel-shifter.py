import Adafruit_BBIO.GPIO as GPIO
from time import sleep
from random import randint
# SER   = Data
# RCLK  = Latch
# SRCLK = Clock
# SRCLR = Clear (keep high)
# OE    = Blank (keep low)

Data1  = "P9_23"
Clock1 = "P9_27"
Latch1 = "P9_25"
Data2  = "P8_14"
Clock2 = "P8_18"
Latch2 = "P8_16"

GPIO.setup(Data1, GPIO.OUT)
GPIO.setup(Clock1, GPIO.OUT)
GPIO.setup(Latch1, GPIO.OUT)
GPIO.setup(Data2, GPIO.OUT)
GPIO.setup(Clock2, GPIO.OUT)
GPIO.setup(Latch2, GPIO.OUT)

global hook

def delay(millis):
    millis_to_seconds = float(millis)/1000
    return sleep(millis_to_seconds)


def shift(data, clock, latch, speed):
  new_data = randint(0, 1)
  hook = new_data
  if new_data == 0:
    GPIO.output(data, GPIO.HIGH)
    GPIO.output(clock, GPIO.HIGH)
    GPIO.output(clock, GPIO.LOW)
    GPIO.output(data, GPIO.LOW)
  if new_data == 1:
    GPIO.output(clock, GPIO.HIGH)
    GPIO.output(clock, GPIO.LOW)
  GPIO.output(latch, GPIO.HIGH)
  GPIO.output(latch, GPIO.LOW)
  delay(int(speed))

def static_shift(data, clock, latch, odds):
  data_string = []
  triger = randint(0,int(odds))
  if triger == 1:
    for i in range(32):
      digit = str(randint(0, 1))
      data_string.append(digit)
    for bits in data_string:
      if bits == '0':
        GPIO.output(data, GPIO.HIGH)
        GPIO.output(clock, GPIO.HIGH)
        GPIO.output(clock, GPIO.LOW)
        GPIO.output(data, GPIO.LOW)
      if bits == '1':
        GPIO.output(clock, GPIO.HIGH)
        GPIO.output(clock, GPIO.LOW)
    GPIO.output(latch, GPIO.HIGH)
    GPIO.output(latch, GPIO.LOW)

def clear_leds(data, clock, latch, leds):
  for i in range(leds):
    GPIO.output(data, GPIO.HIGH)
    GPIO.output(clock, GPIO.HIGH)
    GPIO.output(clock, GPIO.LOW)
    GPIO.output(data, GPIO.LOW)
  GPIO.output(latch, GPIO.HIGH)
  GPIO.output(latch, GPIO.LOW)

try:
  while True:
    shift(Data1, Clock1, Latch1, 200)
    static_shift(Data2, Clock2, Latch2, 10)
except KeyboardInterrupt:
  print "Stopped by user"
  clear_leds(Data1, Clock1, Latch1, 16)
  clear_leds(Data2, Clock2, Latch2, 16)
  GPIO.cleanup() 