import socket
																				
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('10.42.234.66', 2222))
s.listen(5)
client, address = s.accept()
while True:
	print(address)
	data = s.recv(1024)
	clent.setimeout(60)
	client.close() 
	if bytes('close'.encode('utf-8')) in data:
		s.close()
		break;
	if data:
		clinet.send(data)