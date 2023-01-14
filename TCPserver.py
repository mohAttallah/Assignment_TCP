import socket
# create  a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12000
server_address = ('localhost', port)
print(f'starting up on  {port}  {server_address}')
# bind the socket to the port and ip Address
sock.bind(server_address)
# listen for incoming connections
sock.listen(1)
while True:
    print('wating for a connection')
    connection, client_address = sock.accept()
    try:
        print('client connected :', client_address)
        data = "welcome to  TCP server input saentence (Sent  bay to end communication )"
        connection.sendall(data.encode("UTF-8"))
        while True:
            data = connection.recv(1024).lower()
            print(f'received::  {data.decode("UTF-8")} ')
            if data == "bay".encode("UTF-8"):
                connection.sendall(("GoodBay").encode("UTF-8"))
                connection.close()
                break

            elif data:
                connection.sendall(("OK").encode("UTF-8"))
            else:
                break
    finally:
        connection.close()
