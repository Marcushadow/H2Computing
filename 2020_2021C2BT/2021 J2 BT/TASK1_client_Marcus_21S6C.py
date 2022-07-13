import socket

clientSock = socket.socket()
clientSock.connect(("127.0.0.1", 12345))

receivedMsg = clientSock.recv(1024)

while(receivedMsg != b"END"):
    if(receivedMsg == b"GUESSL"):
        guess = input("Please guess a letter: ")
    
    elif(receivedMsg == b"GUESSW"):
        guess = input("Please guess a word: ")

    clientSock.sendall(guess.encode())
    receivedMsg = clientSock.recv(1024)
    print(receivedMsg.decode())

    receivedMsg = clientSock.recv(1024)


clientSock.close()