import socket

newSocket = socket.socket()
newSocket.bind(('127.0.0.1', 12345))

newSocket.listen()

receivedSocket , addr = newSocket.accept()

print('Connected to: ' + str(addr))
receivedSocket.sendall(b'Hello Asher is 187\n')
receivedSocket.close()
newSocket.close()