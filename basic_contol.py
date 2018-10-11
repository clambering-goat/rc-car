import machine

import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
#0.0.0.0 is it root ip to acces from pc go to 192.168.4.1
s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)
cl, addr = s.accept()
print(addr," has connect")
while True:
    print("runing")


    x=s.recv(5)
    print(x)
cl.close()
