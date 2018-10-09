import socket

CHUNK_SIZE = 8 * 1024

server_socket = socket.socket()
server_socket.bind(('192.168.0.5', 5000))
server_socket.listen(5)
client_socket, addr = server_socket.accept()

data = "hello world "
while data:
    client_socket.send(data)
client_socket.close()
