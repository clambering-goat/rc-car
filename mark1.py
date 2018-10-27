
def start():
    import machine
    import socket


    pin5=machine.Pin(5,machine.Pin.OUT)
    pin4=machine.Pin(4,machine.Pin.OUT)
    pin0=machine.Pin(0,machine.Pin.OUT)
    pin2=machine.Pin(2,machine.Pin.OUT)
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    #0.0.0.0 is it root ip to acces from pc go to 192.168.4.1
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind(addr)
    s.listen(1)

    print('listening on', addr)
    cl, addr = s.accept()
    print(addr," has connect")
    while True:
        print("runing")


        x=cl.recv(10)
        x=x.decode()

        if x =="stop":
            pin5.on()
            pin4.on()
            pin0.on()
            pin2.on()
            print("stoping")
        if x =="close":
            break

        if x =="forward":
            print("forward")
            pin5.off()
            pin4.on()

        if x =="back":
            print("back")
            pin5.on()
            pin4.off()

        if x=="right":
            print("right")
            pin0.off()
            pin2.on()

        if x=="left":
            print("left")
            pin0.on()
            pin2.off()


    cl.close()
    s.close()
    print("connect closed")
