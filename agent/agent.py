import socket

s = socket.socket()

PORT = 8888
HOST = "127.0.0.1"

s.connect((HOST, PORT))
s.send("Hi there".encode())
s.close()
