import time
import socket
import sys

print("\nChat Room 1-0-1\n")
s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
print(host, "(", ip, ")\n")

host = input("Enter server address: ")
name = input("\nEnter your name: ")
port = 1234

s.connect((host, port))
print("Connected.\n")
s.send(name.encode())

s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room")
print("Enter e to exit the chat room\n")

while True:
    message = s.recv(1024)
    message = message.decode()
    print(s_name, ":", message)
    message = input("Me: ")
    if message == "e":
        message = "Left the chat room!"
        s.send(message.encode())
        print("\n")
        break
    s.send(message.encode())
