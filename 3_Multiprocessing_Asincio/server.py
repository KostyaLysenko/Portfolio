import socket
import asyncio
sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('',55000))
sock.listen(20)
print('Server is running')
while True:
    conn, addr = sock.accept()
    print('connected', addr)
    data= conn.recv(1024)
    print("recieved {!r}".format(data))
    input_data = data.decode().split()
    async def function_1():
        await asyncio.sleep(2)
        return conn.sendall(str(eval(str(int(input_data[0]) - int(input_data[1])))).encode()), \
            print(str(eval(str(int(input_data[0]) - int(input_data[1])))).encode())

    async def function_2():
        await asyncio.sleep(1)
        return conn.sendall(str(eval(str(int(input_data[0]) + int(input_data[1])))).encode()), \
            print(str(eval(str(int(input_data[0]) + int(input_data[1])))).encode())

    async def function_3():
        await asyncio.sleep(0)
        return conn.sendall(str(eval(str(int(input_data[0]) * int(input_data[1])))).encode()), \
            print(str(eval(str(int(input_data[0]) * int(input_data[1])))).encode())

    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(function_1()), ioloop.create_task(function_2()), ioloop.create_task(function_3())]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)

conn.close