import socket
import threading

# Our list of clients that are currently connected.
clients_lock = threading.Lock()
connected_clients = []

address = ('localhost', 10000)

# Creating a TCP socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to the address.
sock.bind(address)

# Opens the socket.
print("Opening socket 10000...")

sock.listen(1)

print("Server now listening.")

# Thread function to process a specific connected client.
def process_client(connection):
    while True:
        try:
            data = connection.recv(1000)    # Blocking!

            if data:
                print(data.decode())
        except:
            # Something happened, like the client disconnecting.
            connection.close()
            print("\nClient disconnected!\n")
            
            with clients_lock:
                # TODO: Remove my connection from the list...
                pass

            break

while True:
    # Blocking call waiting for a client.
    print("Waiting for connection...")

    connection, client_address = sock.accept()

    print("\nClient connected.\n")

    # Add the client to a list.
    with clients_lock:
        connected_clients.append((connection, client_address))

    # Start a thread that manages listening for data from the client.
    t = threading.Thread(target=process_client, args=(connection,))
    t.start()



        












