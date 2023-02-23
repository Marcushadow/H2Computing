import socket

serverSocket = socket.socket()

serverSocket.bind(("127.0.0.1", 12345))

serverSocket.listen()

returnSocket, addr = serverSocket.accept()

returnSocket.sendall("Welcome to server".encode())

returnObj = b""

while(returnObj != b"quit"):
    returnObj = b""
    while(b"\\n" not in returnObj):
        socketMsg = returnSocket.recv(1024)
        returnObj += socketMsg

    print(returnObj.decode().strip("\\n"))

    returnSocket.send("Continue!".encode())