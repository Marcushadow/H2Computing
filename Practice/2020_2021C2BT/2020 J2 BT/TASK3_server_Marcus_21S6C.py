import socket, random

randomCharacter = chr(random.randint(ord('A'), ord('Z') + 1))

mySocket = socket.socket()
mySocket.bind(("127.0.0.1", 12345))
mySocket.listen()

newSocket, addr = mySocket.accept()

print("To guess:", randomCharacter)
guessed = False

while(guessed == False):
    newSocket.sendall(b"Please make another guess: \n")
    
    reply = b""
    while(b"\n" not in reply):
        value = newSocket.recv(1024)
        reply = reply + value
        
    
    
    guess = reply.decode()[0]
    print(guess)
    
    if (guess[0] == randomCharacter):
        newSocket.sendall(b'WIN\n')
        guessed = True
        
    else:
        newSocket.sendall(b"WRONG Make another guess\n")
    
    




newSocket.close()

