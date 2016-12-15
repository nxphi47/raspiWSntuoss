"""
First tutorial
Blinking and button
"""

# import GPIO module
import RPi.GPIO as GPIO
import time


GPIO.VERSION
# set the mode of GPIO
GPIO.setMode(GPIO.BOARD)

ledPin = 11	# onboard, 17 BCM
buttonPin = 13	# onboard, 27 BCM
pwmPin = 12 #onboard 12

# setmode for the pin
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN)
GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 1000) #1KHz of Pulse width modulation


# loop function
def blinking():
	while True:
		print "Out HIGH"
		GPIO.output(ledPin, GPIO.HIGH)
		time.sleep(0.5)
		print "Out LOW"
		GPIO.output(ledPin, GPIO.LOW)
		time.sleep(0.5)


def blinkWithButton():
	while True:
		buttonIn = GPIO.input(buttonPin)
		if buttonIn:
			print "Button pressed, out with 0.25 period"
			print "Out HIGH"
			GPIO.output(ledPin, GPIO.HIGH)
			time.sleep(0.25)
			print "Out LOW"
			GPIO.output(ledPin, GPIO.LOW)
			time.sleep(0.25)
		else:
			blinking()


def dimming():
	val = 0
	try:
		pwm.start(val)
		while True:
			if val > 1:
				val = 0
			pwm.changeDutyCycle(val)
			time.sleep(0.05)
			val += 0.1
	except KeyboardInterrupt:
		pwm.stop()
		GPIO.cleanup()



#where the program begin
try:
	blinking()
except KeyboardInterrupt:
	GPIO.cleanup()