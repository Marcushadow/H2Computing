import socket

clientSock = socket.socket()
clientSock.connect(("127.0.0.1", 12345))

received = b""
while(b"\n" not in received):
    received += clientSock.recv(1024)

while(received != b"WIN\n" and b"LOSE\n" not in received):
    guess = input("Guess a number between 1 and 100: ")
    message = guess.encode() + b"\n"

    clientSock.sendall(message)

    received = b""
    while(b"\n" not in received):
        received += clientSock.recv(1024)

    if(received == b"LOWER\n"):
        print("Guess Lower")

    elif(received == b"HIGHER\n"):
        print("Guess Higher")


if(b"LOSE\n" in received):
    correct = received.decode().strip("\n").split("\n")[-1]
    
    print("You ran out of tries, the correct answer is", correct)

elif(received == b"WIN\n"):

    print("You won!")

clientSock.sendall(b"Game closed.\n")
clientSock.close()
