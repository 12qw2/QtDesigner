"""
1. 导入模块socket
2. 创建socket套接字
3. 绑定IP&端口（可选）
4. 发送数据
5. 关闭套接字
"""

# 导入模块 socket
import socket

# 创建 socket 套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定 IP 地址和端口
udp_socket.bind(('127.0.1.1', 8080))

# 发送数据
udp_socket.sendto(b'Hello, world!', ('127.0.1.1', 8081))

# 关闭套接字
udp_socket.close()
