import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print (sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    sock.sendall('SERVICER'.encode())
    # Send data
    img = open("IMG_2957.JPG", "rb")
    sock.sendall(img.read())
    img.close()


finally:
    print (sys.stderr, 'closing socket')
    img.close()
    sock.close()
