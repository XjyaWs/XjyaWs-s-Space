import socket

client = socket.socket()
client.connect(('127.0.0.1', 8080))

client.send(b'Hello world!')

data = client.recv(1024)
print(data.decode('utf-8'))
client.close()
