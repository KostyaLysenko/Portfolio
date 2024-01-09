import socket

sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
#
# sock.send(bytes("What is your name?", encoding='UTF-8'))
# sock.send(bytes("This is client, answer me!", encoding='UTF-8'))
sock.send(bytes(input(), encoding='UTF-8'))

data= sock.recv(1024)
sock.close()
print(data)


