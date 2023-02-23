import socket
import time
from _thread import *

my_socket = socket.socket()

address = "127.0.0.1"
port = 12345

my_socket.connect((address, port))



print(my_socket.recv(1024).decode())
while True:
    
    text = input("Message: ")
    my_socket.sendall(text.encode())

    print(f"\nIncoming Message: \n {my_socket.recv(1024).decode()} \n")





my_socket.close()