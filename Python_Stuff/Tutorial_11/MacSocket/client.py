import socket

clientSocket = socket.socket()

clientSocket.connect(("127.0.0.1", 12345))

print(clientSocket.recv(1024).decode())

msg = input("Enter your message: ")
while(msg != "quit"):
    if ("\\n" not in msg):
        clientSocket.sendall(msg.encode())
        msg = input("Enter your message: ")

    else:
        clientSocket.sendall(msg.encode())
        print(clientSocket.recv(1024).decode())
        msg = input("Enter your message: ")