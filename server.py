import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print (sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

temp = bytearray()
while True:
    # Wait for a connection

    print (sys.stderr, 'waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print (sys.stderr, 'connection from', client_address)
        temp = bytearray()
        while True:
            data = connection.recv(3000)
            temp += data
            if not data:
                print (sys.stderr, 'no more data from', client_address)
                break           
    finally:
        # Clean up the connection
        image = open("mytemp.jpg", "wb")
        image.write(temp)
        image.close()
        connection.close()
        temp = bytearray()
        break

