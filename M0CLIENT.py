import socket
import select
import sys
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=4007
client_socket.connect(('127.0.0.1',port)) 
while True:
 message=input("enter your message: ")
 client_socket.send(message.encode())
 if message=="CLOSE SOCKET":
  client_socket.close()
  break
 else:
     client_socket.send(bytes(message.encode()))
     data =client_socket.recv(1024).decode()
     print(data)
