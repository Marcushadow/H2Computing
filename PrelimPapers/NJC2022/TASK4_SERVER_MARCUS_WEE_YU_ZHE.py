import socket, sqlite3

serverSocket = socket.socket()
serverSocket.bind(("127.0.0.1", 12345))

serverSocket.listen()

sock, addr = serverSocket.accept()

menu = """
1. Highest high tide with one corresponding date and time it happened
2. Lowest low tide with one corresponding date and time it happened
3. Largest tidal range
4. Smallest tidal range

Select using a number (1-4)
"""

sock.sendall(menu.encode())


option = sock.recv(1024).decode()


if(option == "1"):
    client = sqlite3.connect("tide.db")
    curr = client.execute("SELECT Date, MAX(HEIGHT) FROM Tide")
    curr = list(list(curr)[0])
    for i in range(len(curr)):
        curr[i] = str(curr[i])
    output = ",".join(curr)

    sock.sendall(output.encode())
    client.close()

elif(option == "2"):
    client = sqlite3.connect("tide.db")
    curr = client.execute("SELECT Date, MIN(HEIGHT) FROM Tide")
    curr = list(list(curr)[0])
    for i in range(len(curr)):
        curr[i] = str(curr[i])
    output = ",".join(curr)

    sock.sendall(output.encode())
    client.close()
    
elif(option == "3"):
    client = sqlite3.connect("tide.db")
    curr = client.execute("SELECT HEIGHT FROM Tide")
    arr = list(curr)
    largestRange = 0

    for i in range(1, len(arr)):
        newRange = arr[i][0]- arr[i-1][0]
        if(newRange > largestRange):
            largestRange = newRange

    
    sock.sendall(str(largestRange).encode())
    client.close()
    
elif(option == "4"):
    client = sqlite3.connect("tide.db")
    curr = client.execute("SELECT HEIGHT FROM Tide")
    arr = list(curr)
    smallestRange = arr[1][0]-arr[0][0]

    for i in range(2, len(arr)):
        newRange = arr[i][0]- arr[i-1][0]
        if(newRange < smallestRange and newRange > 0):
            smallestRange = newRange

    
    sock.sendall(str(smallestRange).encode())
    client.close()
    
reply = sock.recv(1024)
if(reply == b"END"):
    print("END OF SERVER")

sock.close()
