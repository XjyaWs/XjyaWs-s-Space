"""
4.利用subprocess模块、struct模块及上述你自己解决粘包问题的思路实现简单的客户端远程操控服务端执行命令并将相应的结果再返回给客户端
"""
import socket
import struct

client = socket.socket()
client.connect(('127.0.0.1', 8080))

comm = input('$>>>:').strip()

# 发送指令
client.send(comm.encode('utf-8'))

# 接收返回报头
reply_size = struct.unpack('i', client.recv(4))[0]

# 接收返回内容
reply = client.recv(int(reply_size)).decode('gbk')

print(reply)

client.close()
