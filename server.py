import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print (sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)

sock.listen(1)

lastCount = 0
while True:
    print (sys.stderr, 'waiting for a connection')
    connection, client_address = sock.accept()
    
    try:
        clientType = connection.recv(1000).decode()
        if clientType == "SERVICER":
            temp = bytearray()
            while True:
                data = connection.recv(3000)
                temp += data
                if not data:
                    print (sys.stderr, 'no more data from', client_address)
                    break
            image = open("mytemp.jpg", "wb")
            image.write(temp)
            image.close()
        else:
            http_response = """HTTP/1.1 200 OK

"""
            #append html here
            http_response += "<body>There were no cars seen</body>"
            connection.sendall(str.encode(http_response))
    finally:
        connection.close()
