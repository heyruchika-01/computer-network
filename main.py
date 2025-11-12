import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

sock.listen(1)

while True:
   
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address)

        while True:
            data = connection.recv(1600)
            print('received "%s"' % data)
            if data:
                print('sending data back to the client')
                msg = str(data)
                msg = msg + ' plus extra from the server'
                msg = bytes(msg, 'utf-8')
                connection.sendall(msg)
            else:
                print('no more data from', client_address)
                connection.close()
                break

    finally:
        
        connection.close()