# 导入 socket 模块
import socket

# 导入 utils 模块
from utils import decode_data

# 创建套接字对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定ip和端口
s.bind(('127.0.0.1', 8080))

# 设置端口可以重用
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 设置套接字为被动模式
s.listen(128)

while True:
    # 等待客户端连接(阻塞当前线程，有新客户端接入时才释放阻塞)
    client_socket, client_addr = s.accept()
    print('客户端连接成功:', client_addr)
    
    while True:
        # 接收客户端发送的数据
        data = client_socket.recv(1024)
        
        # 如果接收数据 打印接收到的数据
        if data:
            print('客户端发送的数据:', decode_data(data))
            
            # 发送数据给客户端
            client_socket.send("服务器收到数据了！".encode('utf-8'))
            client_socket.send(data)
        else:
            # 收到空数据，输出数据
            print(data,type(data))
            
            # 提示客户端断开连接
            print('客户端断开连接',data)
            # 如果客户端断开连接，关闭套接字
            client_socket.close()
            break
        

