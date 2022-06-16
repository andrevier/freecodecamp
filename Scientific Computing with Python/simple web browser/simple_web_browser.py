# A simple web browser where the client make the connection with an address
# and get the data.
import socket

# Type of the connection: TCP
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

# An infinit loop to recive the data from the server and print the message. 
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end = " ")
mysock.close()