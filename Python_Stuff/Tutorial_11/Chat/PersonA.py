import socket

serverSocket = socket.socket()

serverSocket.bind(("127.0.0.1", 12345))
serverSocket.listen()

receivedSocket , addr = serverSocket.accept()

print(f"Incoming Message: \n {receivedSocket.recv(1024).decode()} \n")

while True:
    text = input("Message: ")
    receivedSocket.sendall(text.encode())

    print(f"\nIncoming Message: \n {receivedSocket.recv(1024).decode()} \n")

receivedSocket.close()

