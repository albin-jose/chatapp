import socket
import threading

host = 				#give the host address of the system where server.py is running
port =				#specify the same port number assigned to the port in server.py

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

name = input("Enter your name:")
print("Enter message")

def send_msg():
	while True:
		msg = input()
		s_msg = name + '> ' + msg
		s.send(str.encode(s_msg))

def receive_msg():
	while True:
		received_msg = s.recv(2048)
		print(received_msg.decode('utf-8'))


send_msg_thread = threading.Thread(target = send_msg, daemon = True)
receive_msg_thread = threading.Thread(target = receive_msg, daemon = True)

send_msg_thread.start()
receive_msg_thread.start()

send_msg_thread.join()
receive_msg_thread.join()
