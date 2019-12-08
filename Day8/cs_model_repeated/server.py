import socket

server = socket.socket()
server.bind(('127.0.0.1', 8080))
server.listen(5)

while True:     # 链接循环
    conn, addr = server.accept()

    while True:      # 通信循环
        try:
            data = conn.recv(1024)
            if len(data) == 0:
                break
            print(data.decode('utf-8'))
            conn.send(data.upper())
        except Exception as e:
            print(e)
            break
        """
        try 为了解决windows客户端关闭报错
        检测data是否为空为了解决mac linux客户端报错循环打印空行的问题
        """

    conn.close()


