import time
import socket
import sys

print("\nChat Room 1-0-1 \n")

# create a socket object
s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234

s.bind((host, port))
print(host, "(", ip, ")\n")

name = input("Enter your name: ")
s.listen(1)
print("\nWaiting for incoming connections...\n")

conn, addr = s.accept()
print("Received connection from", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room")
print("Enter e to exit the chat room\n")
conn.send(name.encode())

while True:
    message = input("Me: ")
    if message == "e":
        message = "Left the chat room!"
        conn.send(message.encode())
        print("\n")
        break
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(s_name, ":", message)
