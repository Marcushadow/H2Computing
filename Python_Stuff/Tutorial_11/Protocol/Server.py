import socket

serverSocket = socket.socket()

serverSocket.bind(("127.0.0.1", 12345))
serverSocket.listen()

receivedSocket , addr = serverSocket.accept()

returnObject = b''

while (not b'\n' in returnObject):
    returnObject += receivedSocket.recv(1024)

print(returnObject.decode())

receivedSocket.close()

