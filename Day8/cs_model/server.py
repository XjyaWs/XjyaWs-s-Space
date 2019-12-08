import socket

server = socket.socket()  # 括号内什么都不写，默认基于TCP协议的套接字通信
server.bind(('127.0.0.1', 8080))  # bind(元组：ip地址，端口) 127.0.0.1是本地回环地址
server.listen(5)  # 监听 半连接池

conn, addr = server.accept()

data = conn.recv(1024)  # receive message
print(data.decode('utf-8'))

conn.send('Hello!'.encode('utf-8'))  # send message
conn.close()  # connection closed
server.close()   # server closed
