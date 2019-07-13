import socket
import threading

host = 				#give the host address of the system where server.py is running
port =				#specify the same port number assigned to the port in server.py

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

