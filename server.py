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

name = input("Enter your name: ")
print("Enter meaasge")

def send_msg():
	while True:
		msg = input()
		s_msg = name + '> ' + msg
		conn.send(str.encode(s_msg))


def receive_msg():
	while True:
		received_msg = conn.recv(2048)
		print(received_msg.decode('utf-8'))


send_msg_thread = threading.Thread(target = send_msg, daemon = True)
receive_msg_thread = threading.Thread(target = receive_msg, daemon = True)

send_msg_thread.start()
receive_msg_thread.start()

send_msg_thread.join()
receive_msg_thread.join()
