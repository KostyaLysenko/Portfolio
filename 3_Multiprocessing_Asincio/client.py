import socket

sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))

a = "10"
b = "5"

message = ' '.join((a,b))

sock.send(message.encode())
data= sock.recv(1024)
res=data.decode()
print(res)
sock.close()
print(data)
