import socket
import threading



host = ''
port = 			#specify an uncommon port number

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as e:
	print("socket creation error." + str(e))

try:
	s.bind((host, port))
	s.listen()
except socket.error as e:
	print('Socket binding error.' + str(e))

conn, address = s.accept()
print(f"Connection has been established with {address}")

