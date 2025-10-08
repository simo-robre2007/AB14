from movimenti import AlphaBot

import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(("0.0.0.0", 7000))
robot.Alphabot

while True:
    msg, address = server_socket.recvfrom(1024)
    print(msg.decode())
    if (msg == 'w')
        robot.forward(2)
        A = 'Avanti'
        server_socket.sendto(A.encode(), address)

    if (msg == 's')
        robot.backward(2)
        I = 'Indietro'
        server_socket.sendto(I.encode(), address)

    if (msg == 'a')
         robot.left(2)
        S = 'Sinistra'
        server_socket.sendto(S.encode(), address)

    if (msg == 'd')
        robot.right(2)
        D = 'Destra'
        server_socket.sendto(D.encode(), address)

    if (msg == 'EXIT')
        robot.stop()
    
