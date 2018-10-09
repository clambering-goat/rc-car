import socket


holad=""


sock = socket.socket()
sock.connect(('10.10.0.5', 5000))
chunk = sock.recv(1024)

print("runing555")
while True:
    print("runing")
    chunk = sock.recv(1024)
    if not chunk:
        break
    holad=holad+(chunk.decode())
    print("loop")
print("done")
print(holad)
print("hold")

sock.close()


print(holad)
