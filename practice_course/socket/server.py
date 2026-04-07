
import socket

s = socket.socket()
print("Socket Created")

s.bind(("localhost", 5000))

s.listen(3)
print('Waiting for connections')

while True:
   c, addr = s.accept()
   print("Connected with ", addr)

   c.send(bytes("Welcome to miracle's socket connection", "utf-8"))

   print(c.recv(1024).decode())

   c.close()