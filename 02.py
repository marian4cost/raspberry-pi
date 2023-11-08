import RDI.GPIO on GPIO
import time 

est = input("qualo estado do motor (l/d):")

in1 = 23
in2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

if (est == 'l' or est == 'L'):
	print("o motor está ligado")
	GPIO.output(in1, GPIO.HIGH)
	GPIO.output(in2, GPIO.LOW)

elif (est == 'n' or est == 'N'):
	print("o motor está desligado")
	GPIO.output(in1, GPIO.LOW)
	GPIO.output(in2, GPIO.LOW)

else:
	print("digite um valor valido")

