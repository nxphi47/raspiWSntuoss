"""
TUT 1: control the 7 segment digit value from the command line or button
----7---
|		|
9		6
|		|
----10---
|		|
1		4
|		|
----2----
modification:
make it count 0 - 9
make button to control
"""

# import GPIO module
import RPi.GPIO as GPIO
import time

# set the mode of GPIO
GPIO.setmode(GPIO.BOARD)

# LED pins 10  9   7   6   1   2   4, connect to GPIO board pins 11, 12, 13, 15, 16, 18, 22
ledPins = [11, 12, 13, 15, 16, 18, 22]

# digit 0,1,2,3,4,5,6,7,8,9, and nothing
digits = [[0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 1], [1, 0, 1, 1, 1, 1, 0], [1, 0, 1, 1, 0, 1, 1],
		  [1, 1, 0, 1, 0, 0, 4], [1, 1, 1, 0, 0, 1, 1],
		  [1, 1, 1, 0, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1],
		  [0, 0, 0, 0, 0, 0, 0]]

# setmode for pins
for i in ledPins:
	GPIO.setup(i, GPIO.OUT)


def readInput():
	val = raw_input("Enter the number: ")
	val = val[0]
	if not val.isdigit():
		print "WRONG! please enter number!"
		return 0
	else:
		return int(val)


def writeDigit(val):
	# FIXME: edit the following code here, output high for the digit
	for i in ledPins:
		GPIO.output(i, GPIO.LOW)
	for index, value in enumerate(digits[val]):
		GPIO.output(ledPins[index], value)
	pass


# main function goes here, return the digit from the command line
if __name__ == '__main__':
	try:
		writeDigit(10)
		while True:
			time.sleep(0.05)
			writeDigit(readInput())
	except KeyboardInterrupt:
		GPIO.cleanup()
