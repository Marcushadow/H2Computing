import socket
import random

toGuess = random.randint(1, 100)
guessCounter = 10


s = socket.socket()
s.bind(("127.0.0.1", 9999))

s.listen()

returnSocket , addr = s.accept()

returnSocket.sendall("GUESS\n".encode())

value = returnSocket.recv(1024).decode()

while(guessCounter >= 0):
    try:
        value = int(value)
        # print(value, toGuess)
        
        if(value == toGuess):
            returnSocket.sendall("WIN\n".encode())
            break

        elif(value > toGuess and guessCounter > 0):
            guessCounter -= 1
            returnSocket.sendall("HIGH\nGUESS\n".encode())

        elif(value < toGuess and guessCounter > 0):
            guessCounter -= 1
            returnSocket.send("LOW\nGUESS\n".encode())

        else:
            guessCounter -= 1
            returnSocket.send("GAMEOVER\n".encode())


    except:
        returnSocket.sendall("GUESS\n".encode())

    value = returnSocket.recv(1024).decode()
