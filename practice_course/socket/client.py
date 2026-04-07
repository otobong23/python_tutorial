
import socket

c = socket.socket()

c.connect(("localhost", 5000))

print(c.recv(1024).decode())
c.send(bytes("Greetings from client", "utf-8"))