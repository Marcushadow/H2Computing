import socket
import time

my_socket = socket.socket()

address = "192.168.187.26"
port = 12345

my_socket.connect((address, port))

print(f"\nIncoming Message: \n {my_socket.recv(1024).decode()} \n")
while True:
    text = input("Message: ")
    text = text + "\n"
    my_socket.sendall(text.encode())

    print(f"\nIncoming Message: \n {my_socket.recv(1024).decode()} \n")





my_socket.close()