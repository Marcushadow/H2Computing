import socket

client_sock = socket.socket()
client_sock.connect(("127.0.0.1", 12345))

guessed = False

while (guessed == False):
    reply = b""
    while (b"\n" not in reply):
        value = client_sock.recv(1024)
        reply = reply + value
        
    
    
    if (reply == b"WIN\n"):
        guessed = True
        
    elif(guessed == False):
        print(reply.decode())
        Guess = input()
        Guess = Guess.encode() + b"\n"

        client_sock.sendall(Guess)


client_sock.close()