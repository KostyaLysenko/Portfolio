import socket
sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('',55000))
sock.listen(10)
print('Server is running, please press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('connected', addr)
    data= conn.recv(1024)
    print(str(data))
    #авдання 2

    if bytes("What is your name?", encoding='UTF-8') in data:
        conn.send(bytes("SERVERRRRR", encoding='UTF-8'))
    if bytes("Where are you?", encoding='UTF-8') in data:
        conn.send(bytes("I'm in your HEAD!!!", encoding='UTF-8'))

    #Завдання 3
    if bytes("words", encoding='UTF-8') in data:
        conn.send(bytes(f'Quantity of your words is {len(str(data).split())}', encoding='UTF-8'))
    else:
        conn.send(data.upper())
conn.close
