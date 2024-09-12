"""
1. 导入模块socket
2. 创建socket套接字
3. 绑定IP&端口（可选）
4. 接收数据
5. 关闭套接字
"""

# 1. 导入模块socket
import socket

# 2. 创建socket套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 3. 绑定IP&端口（可选）
s.bind(('127.0.0.1', 8888))


# 4. 接收数据
while True:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    print(data.decode('utf-8'))

# 5. 关闭套接字
s.close()