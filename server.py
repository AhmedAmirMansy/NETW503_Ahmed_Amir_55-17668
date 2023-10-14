import socket
import select
import sys
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=4007
server_socket.bind(('127.0.0.1',port))
server_socket.listen(port)
while True :
 client_socket,client_address = server_socket.accept()
 while True:
  message = server_socket.recv(1024).decode('utf-8')
  if message != "CLOSE SOCKET":
   client_socket.close()
   break
  else :
   message.upper()
   client_socket.sendmessage.encode('utf-8')