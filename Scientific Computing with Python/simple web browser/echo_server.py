# Code for a simple server with the socket lib.
# Run the echo_server.py in a terminal;
# Open another terminal and run the echo_client.py
# Observe how they exchange data. 
#
# from https://realpython.com/python-sockets/
# 12/06/22
import socket

# HOST is a standard loopback interface address (localhost)
HOST = "127.0.0.1"

# Port to listen on
PORT = 65432

# Use a TCP and IPv4 to send messages. 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Standard server side procedure: bind, listen and accept.
    s.bind((HOST, PORT))
    s.listen()

    # The .accept() method blocks execution and waits for an incoming
    # connection. When a client connects, it returns a new socket object
    # representing the connection and a tuple holding the address of the client. 
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)