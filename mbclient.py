import socket
import time

# Create the TCP socket we need to make a connection.
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# The addres we want to connect to.
address = ('localhost', 10000)

# Lets connect to a server.
socket.connect(address)

print("Connected!")

count = 0

try:
    while True:
        count += 1
        socket.send(f"Hello there! - {count}".encode())
        time.sleep(5)
except Exception as e:
    print(e)
    print("Closing the socket.")
    socket.close()






