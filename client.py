import socket
import time 

PORT = 12341
time.sleep(1)
# IP = socket.gethostbyname('server')
IP = 'localhost'
s = socket.socket()
s.connect((IP, PORT))
s.send("something".encode())
recv = s.recv(1024)
print(recv)
time.sleep(1)
s.send("alt mesaj".encode())
recv = s.recv(1024)
print(recv)
