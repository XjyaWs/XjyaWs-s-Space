"""
4.利用subprocess模块、struct模块及上述你自己解决粘包问题的思路实现简单的客户端远程操控服务端执行命令并将相应的结果再返回给客户端
"""
import socket
import struct
import subprocess

server = socket.socket()
server.bind(('127.0.0.1', 8080))
server.listen(5)

while True:
    conn, addr = server.accept()

    try:
        # 接收指令
        comm = conn.recv(1024).decode('utf-8')

        sub = subprocess.Popen(
            comm,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # 生成返回指令
        reply = sub.stdout.read() + sub.stderr.read()

        # 生成返回报头
        reply_size = struct.pack('i', len(reply))

        # 发送返回内容报头
        conn.send(reply_size)

        # 发送返回内容
        conn.send(reply)

        conn.close()
    except Exception as e:
        print(e)
        conn.close()
