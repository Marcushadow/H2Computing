import socket, os, random

serverSocket = socket.socket()
serverSocket.bind(("127.0.0.1", 12345))

serverSocket.listen()

s, addr = serverSocket.accept()

filepath = os.path.join("Additional Materials", "WORDS.txt")

with open(filepath) as fs:
    guessList = fs.read().split("\n")
guessWord = guessList[random.randint(0, len(guessList))]

print(guessWord)

guess = 5
while (guess > 0):
    s.sendall(b"GUESSL")

    value = s.recv(1024)
    if value.decode() in guessWord:
        s.sendall(b"YES")
    
    else:
        s.sendall(b"NO")
    
    guess -= 1

s.sendall(b"GUESSW")
value = s.recv(1024)

if(value.decode() == guessWord):
    s.sendall(b"You WIN! The word was " + guessWord.encode())

else:
    s.sendall(b"You LOSE! The word was " + guessWord.encode())

s.sendall(b"END")




s.close()