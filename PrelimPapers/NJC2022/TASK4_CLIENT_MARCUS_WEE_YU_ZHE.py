import socket

clientSock = socket.socket()

clientSock.connect(("127.0.0.1", 12345))

menu = clientSock.recv(1024).decode()
print(menu)


reply = input("What menu option: ")

clientSock.sendall(reply.encode())

outcome = clientSock.recv(1024).decode()
print(outcome)


clientSock.sendall(b"END")
clientSock.close()
