import Adafruit_BBIO.GPIO as GPIO

class ShiftRegister:
    register_type = '74HC595'

    def __init__(self, data_pin, latch_pin, clock_pin):
        self.data_pin = data_pin
        self.latch_pin = latch_pin
        self.clock_pin = clock_pin

        GPIO.setup(self.data_pin, GPIO.OUT)
        GPIO.setup(self.latch_pin, GPIO.OUT)
        GPIO.setup(self.clock_pin, GPIO.OUT)

        self.outputs = [GPIO.LOW] * 8

    def setOutput(self, output_number, value):
        try:
            self.outputs[output_number] = value
        except IndexError:
            raise ValueError("Invalid output number. Can be only an int from 0 to 7")

    def setOutputs(self, outputs):
        if 8 != len(outputs):
            raise ValueError("setOutputs must be an array with 8 elements")

        self.outputs = outputs

    def latch(self):
        GPIO.output(self.latch_pin, GPIO.LOW)

        for i in range(7, -1, -1):
            GPIO.output(self.clock_pin, GPIO.LOW)
            GPIO.output(self.data_pin, self.outputs[i])
            GPIO.output(self.clock_pin, GPIO.HIGH)

        GPIO.output(self.latch_pin, GPIO.HIGH)
