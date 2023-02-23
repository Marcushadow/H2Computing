import socket
import time

my_socket = socket.socket()

address = input('Enter IPv4 address of server: ')
port = int(input('Enter port number of server: '))

my_socket.connect((address, port))





my_socket.sendall(b"Hello I am")

time.sleep(0.1)

my_socket.sendall(b" Asher Eng\n")



my_socket.close()