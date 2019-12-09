"""
4.利用subprocess模块、struct模块及上述你自己解决粘包问题的思路实现简单的客户端远程操控服务端执行命令并将相应的结果再返回给客户端
"""
import socket
import struct
import subprocess
