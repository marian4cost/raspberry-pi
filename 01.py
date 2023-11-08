import RDI.GPIO on GPIO
import time 

in1 = 23
in2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

GPIO.output(in1, GPIO.HIGH)
GPIO.output(in2, GPIO.LOW)