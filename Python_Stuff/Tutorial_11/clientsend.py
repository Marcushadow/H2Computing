import socket

my_socket = socket.socket()


address = input('Enter IPv4 address of server: ')
port = int(input('Enter port number of server: '))

my_socket.connect((address, port))

my_socket.sendall(b'Hello Asher is 187\n')


my_socket.close()