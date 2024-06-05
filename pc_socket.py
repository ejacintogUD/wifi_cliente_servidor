import socket

print("loading librearies")

s = socket.socket()
s.connect(('192.168.26.180', 2024))
print("connected")

while True:
    a = input("Enter the command: ")
    s.send(a.encode())
