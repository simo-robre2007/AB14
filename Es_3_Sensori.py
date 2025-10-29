from Alphabot import AlphaBot
import RPi.GPIO as GPIO
import time

robot = AlphaBot()

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN)
GPIO.setup(16, GPIO.IN)

while True:
	robot.forward()
	time.sleep(0.05)
	if GPIO.input(19) == 0:
		print ('ostacolo SX')
		robot.stop()
		time.sleep(0.5)
		robot.backward()
		time.sleep(0.5)
		robot.right()
		time.sleep(0.5)

	if GPIO.input(16) == 0:
		print ('ostacolo DX')
		robot.stop()
		time.sleep(0.5)
		robot.backward()
		time.sleep(0.5)
		robot.left()
		time.sleep(0.5)

	if GPIO.input(19)== 0 and GPIO.input(16) == 0:
		print ('ostacolo davanti')
		robot.stop()
		time.sleep(0.5)
		robot.backward()
		time.sleep(0.5)
		robot.right()
		time.sleep(0.5)

