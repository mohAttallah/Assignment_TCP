import socket
port = 12000
host = 'localhost'
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# conection  with host(localhost ) and port
s.connect((host, port))
# receive data
data = s.recv(size)
if len(data):
    print('Received:', data.decode('utf-8'))
    data = "message goes here"
    while len(data):
        message = input('input saentence: ')
        s.send(message.encode('utf-8'))
        data = s.recv(size)
        print('Received:', data.decode('utf-8'))
        if data == "GoodBay".encode("UTF-8"):
            data = ''
    s.close()
