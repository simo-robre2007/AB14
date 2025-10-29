from Alphabot import AlphaBot
import time

robot = AlphaBot()
robot.setPWMA(41)
robot.setPWMB(40)


robot.forward()
time.sleep(6.2)

robot.stop()
time.sleep(0.5)

robot.left()
time.sleep(0.5)

robot.stop()
time.sleep(0.5)

robot.forward()
time.sleep(1)

robot.stop()
time.sleep(0.5)

robot.left()
time.sleep(0.6)

robot.stop()
time.sleep(0.5)

robot.setPWMA(42)
robot.setPWMB(42)

robot.forward()
time.sleep(6.5)
