import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 12345
ThreadCount = 0

unsentMessages = []

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)

# def post_message(message):
#     ServerSocket.sendall(data)

def threaded_client(connection, unsentMessage):
    connection.send(str.encode('Connection Established'))
    while True:
        

        data = connection.recv(2048)

        if (data == None):
            print("No")
            continue
        else:
            unsentMessage.append(data.decode())
    
    connection.close()

while True:
    # if(len(unsentMessages) > 0 ):
    #         for item in unsentMessages:
    #         ServerSocket.sendall(item.encode())
            
    #     unsentMessages = []
    


        
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, unsentMessages))


    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))


ServerSocket.close()