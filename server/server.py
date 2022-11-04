import socket

HOST='127.0.0.1'
PORT=8888
s = socket.socket()
s.bind((HOST, PORT))

s.listen(5)

while True:
    c, addr = s.accept()
    print ('Recieved connection :', addr)
    print (c.recv(1024).decode())
    c.close()

