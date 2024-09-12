""" 
tcp协议 作为 服务器 编程流程
1. socket 创建套接字
2. bin 绑定 ip 和 port
3. listen 使套接字设置成被动模式
4. accept 等待客户端的连接
5. recv / send 接收 发送数据

"""

# 导入 socket
import socket
# 1. socket 创建套接字
tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 2. bind 绑定 ip 和 port
tcp_server_socket.bind(("127.0.0.1", 8080))
# s.bind(("127.0.0.1", 8888))

# 3. listen 使套接字设置成被动模式
# 参数：等待客户端的链接的最大数量，只在Windows里生效，其他系统不限制
# 此时，socket套接字对象由主动连接模式变为被动模式, 等待客户端接入
tcp_server_socket.listen(128)

# 4. accept 等待客户端的连接
print("服务器已开启，等待客户端接入！")
# tcp_client 客户端  client_addr 客户端 ip 和 port
tcp_client, client_addr = tcp_server_socket.accept()
print("有新的客户端来了：", client_addr)

# 获取客户端的IP地址
client_ip = client_addr[0]
print(f"已连接的客户端IP地址: {client_ip}")

# 5. 等待接收客户端的数据 1024是缓冲区的大小
client_dada = tcp_client.recv(1024)
print("收到来自客户端的数据：", client_dada.decode("GBK"))
# 6. 将客户端的数据返回
tcp_client.send(client_dada)

# 7. 关闭服务器
tcp_server_socket.close()

