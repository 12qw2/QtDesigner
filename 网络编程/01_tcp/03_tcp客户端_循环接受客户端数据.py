# 导入 socket 模块
import socket

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定 IP 地址和端口号
s.bind(('127.0.0.1', 8080))


# 设置被动模式
s.listen(1024)

# 建立客户端对象
client_socket, client_address = s.accept()

# 循环接受客户端数据
while True:
    # 接收数据
    data = client_socket.recv(1024)
    if not data:
        break
    # 打印接收到的数据
    print(data.decode('utf-8'))

# 关闭 socket
s.close()