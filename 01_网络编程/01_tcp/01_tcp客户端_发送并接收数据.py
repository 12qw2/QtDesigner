"""
1. 导入 socket 模块
2. 创建 socket 套接字
3. 建立 tcp 连接 （连接到服务器）
4. 发送数据 
5. 关闭套接字
"""

# 1 导入 socket 模块
import socket

# 2. 创建socket套接字
# 参数1：地址簇，地址类型family: AddressFamily | int 
#       AF_INET     IPv4
#       AF_INET6    IPv6
# 参数2：协议类型 type: SocketKind | int
#       SOCK_STREAM     TCP协议
#       SOCK_DGRAM      UDP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3 建立 tcp 连接 （连接到服务器）
s.connect(("127.0.0.1", 8080))


# 4 发送数据
s.send("Hello, world!".encode("utf-8"))

# 5 接收数据 等待服务器返回数据
recv_data = s.recv(1024) #收到的是 字节序列

# 将收到的字节序列 按 GBK 格式 解码 成 字符串 输出
print("收到服务器的数据",recv_data.decode(encoding="GBK")) 


# 5 关闭套接字
s.close()
