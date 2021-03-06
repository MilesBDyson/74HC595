import Adafruit_BBIO.GPIO as GPIO
from time import sleep
from random import randint

# this file uses two shift registers wired up to bi-color 3-pin LED's 
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
GND --|8     9|-- QH'    <--- DATA OUT to SER on next IC
       -------
'''

Data1 = "P9_23"
Data2 = "P8_14"
Latch = "P9_25"
Clock1 = "P9_27"
Clock2 = "P8_18"
Clear = "P9_24"
Oe = "P9_26"

GPIO.setup(Data1, GPIO.OUT)
GPIO.setup(Data2, GPIO.OUT)
GPIO.setup(Latch, GPIO.OUT)
GPIO.setup(Clock1, GPIO.OUT)
GPIO.setup(Clock2, GPIO.OUT)

GPIO.setup(Clear, GPIO.OUT)
GPIO.setup(Oe, GPIO.OUT)

GPIO.output(Clear, GPIO.HIGH)    #<--- set low to clear the registers
GPIO.output(Oe, GPIO.LOW)        #<--- set HIGH to turn off registers

def delay(millis):
    millis_to_seconds = float(millis)/1000
    return sleep(millis_to_seconds)

def shift(data1, data2, clock1, clock2, latch, speed):

  n0 = randint(0,1)
  n1 = randint(0,1)
  n2 = randint(0,1)
  n3 = randint(0,1)
  if n0 == 0 and n1 == 0:
    new1 = 0
  else:
    new1 = 1
  if n2 == 0 and n3 == 0:
  	 new2 = 0
  else:
    new2 = 1

  #new1 = randint(0, 1)
  #new2 = randint(0, 1)
  if new1 == 0 and new2 == 0:
    GPIO.output(data1, GPIO.HIGH)
    GPIO.output(data2, GPIO.HIGH)
    GPIO.output(clock1, GPIO.HIGH)
    GPIO.output(clock2, GPIO.HIGH)
    GPIO.output(clock1, GPIO.LOW)
    GPIO.output(clock2, GPIO.LOW)
    GPIO.output(data1, GPIO.LOW)
    GPIO.output(data2, GPIO.LOW)
  if new1 == 1 and new2 == 1:
    GPIO.output(clock1, GPIO.HIGH)
    GPIO.output(clock2, GPIO.HIGH)
    GPIO.output(clock1, GPIO.LOW)
    GPIO.output(clock2, GPIO.LOW)
  if new1 == 0 and new2 == 1:
    GPIO.output(data1, GPIO.HIGH)
    GPIO.output(clock1, GPIO.HIGH)
    GPIO.output(clock1, GPIO.LOW)
    GPIO.output(data1, GPIO.LOW)
    GPIO.output(data2, GPIO.LOW)
    GPIO.output(clock2, GPIO.HIGH)
    GPIO.output(clock2, GPIO.LOW)
  if new1 == 1 and new2 == 0:
    GPIO.output(data2, GPIO.HIGH)
    GPIO.output(clock2, GPIO.HIGH)
    GPIO.output(clock2, GPIO.LOW)
    GPIO.output(data2, GPIO.LOW)
    GPIO.output(data1, GPIO.LOW)
    GPIO.output(clock1, GPIO.HIGH)
    GPIO.output(clock1, GPIO.LOW)
  GPIO.output(latch, GPIO.HIGH)
  GPIO.output(latch, GPIO.LOW)
  delay(int(speed))

def clear_leds(data1, data2, clock1, clock2, latch, leds):
  for i in range(leds):
    GPIO.output(data1, GPIO.LOW)
    GPIO.output(data2, GPIO.LOW)
    GPIO.output(clock1, GPIO.HIGH)
    GPIO.output(clock1, GPIO.LOW)
    GPIO.output(clock2, GPIO.HIGH)
    GPIO.output(clock2, GPIO.LOW)
    GPIO.output(data1, GPIO.HIGH)
    GPIO.output(data2, GPIO.HIGH)
  GPIO.output(latch, GPIO.HIGH)
  GPIO.output(latch, GPIO.LOW)

try:
  while True:
    shift(Data1, Data2, Clock1, Clock2, Latch, 100)
except KeyboardInterrupt:
  print "Stopped by user"
  clear_leds(Data1, Data2, Clock1, Clock2, Latch, 16)
  GPIO.cleanup() 