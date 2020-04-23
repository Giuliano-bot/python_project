#!/usr/share/python3
import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.10.7",43))
s.send("exemple.com.br\r\n")
resp = s.recv(1024)
print (resp) 
