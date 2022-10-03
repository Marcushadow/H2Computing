import socket, random

serverSock = socket.socket()
serverSock.bind(("127.0.0.1", 12345))

serverSock.listen()


newSock, addr = serverSock.accept()


firstMsg = "GUESS\n"
guesses = 5
toGuess = random.randint(1,100)
print(toGuess)
guessed = False
newSock.sendall(firstMsg.encode())

while(guesses > 0 and not guessed):
    received = b""
    while(b"\n" not in received):
        received += newSock.recv(1024)

    guess = int(received.strip(b"\n").decode())

    if(guess == toGuess):
        guessed = True
        message = b"WIN\n"

    elif(guess > toGuess):
        message = b"LOWER\n"
        guesses -= 1

    else:
        message = b"HIGHER\n"
        guesses -= 1

    if(guesses == 0):
        message = b"LOSE\n" + str(toGuess).encode() + b"\n"

    newSock.sendall(message)

received = b""
while(b"\n" not in received):
    received += newSock.recv(1024)

print(received.decode())
        
newSock.close()
        

    
    

    
