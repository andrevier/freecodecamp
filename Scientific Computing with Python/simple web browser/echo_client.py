# Code for a simple client with the socket lib.
# Run the echo_server.py in a terminal;
# Open another terminal and run the echo_client.py
# Observe how they exchange data. 
#
# from https://realpython.com/python-sockets/
# 12/06/22

import socket

# The server's hostname or IP address
HOST = "127.0.0.1"

# The port used by the server
PORT = 65432

# Stablishing a TCP with a IPv4
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Standard procedure for client: connect, send and recieve.
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")