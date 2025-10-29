from Alphabot import AlphaBot
import time

import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(("0.0.0.0", 7000))
robot = AlphaBot()
robot.stop()

while True:
	msg1, address = server_socket.recvfrom(1024)
	msg = msg1.decode()
	print(msg)
	if msg == 'w':
		robot.forward()
		time.sleep(2)
		robot.stop()
		A = 'Avanti'
		server_socket.sendto(A.encode(), address)

	if msg == 's':
		robot.backward()
		time.sleep(2)
		robot.stop()
		I = 'Indietro'
		server_socket.sendto(I.encode(), address)

	if msg == 'a':
		robot.left()
		time.sleep(2)
		robot.stop()
		S = 'Sinistra'
		server_socket.sendto(S.encode(), address)

	if msg == 'd':
		robot.right()
		time.sleep(2)
		robot.stop()
		D = 'Destra'
		server_socket.sendto(D.encode(), address)

	if msg == 'EXIT':
		robot.stop()
		break
server_socket.close()
