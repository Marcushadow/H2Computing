
import socket

newSocket = socket.socket()
newSocket.bind(('127.0.0.1', 12345))

newSocket.listen()

receivedSocket , addr = newSocket.accept()

print('Connected to: ' + str(addr))

print(receivedSocket.recv(1024))
receivedSocket.close()
newSocket.close()

