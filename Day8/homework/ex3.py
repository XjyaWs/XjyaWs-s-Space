"""
3.TCP又叫可靠协议、流式协议、如何避免TCP粘包问题，能否简述一下解决思路
"""

"""
关键是知道当前所需要的接受的数据长度是多少
解决方法：
    提前发送数据报头，提前告诉数据接收方数据的长度
    报头的长度必须是固定的（struct模块）
    
"""