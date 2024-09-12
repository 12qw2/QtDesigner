""" 
tcp协议 作为 服务器 编程流程
1. socket 创建套接字
2. bin 绑定 ip 和 port
3. listen 使套接字设置成被动模式
4. accept 等待客户端的连接
5. recv / send 接收 发送数据

"""

""" 
      思路
主函数循环等待客户端的连接
接收客户端的连接后创建子线程处理客户端的请求

"""

# 导入 socket 模块
import socket

# 导入 threading 模块
import threading

# 定义子线程处理客户端的请求
def handle_client(client: socket.socket):
    
    # 给服务器发送数据
    client.send(b'Hello, server!')
    
    while True:
        # 接收客户端的数据
        data = client.recv(1024)
        
        if data:
            # 发送数据给客户端
            client.send(data)
        else:
            # 客户端断开连接
            break
        
        

def main():

    # 创建 socket 对象
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定 ip 和 port
    server.bind(('', 8080))

    # 使套接字设置成被动模式
    server.listen(5)

    # 等待客户端的连接
    while True:
        # 接受客户端的连接
        client, addr = server.accept()
        print('连接地址:', addr)
        
        # 创建子线程处理客户端的请求
        ti = threading.Thread(target=handle_client, args=(client,))
        
        # 设置守护线程
        ti.setDaemon(True)
        
        # 启动子线程
        ti.start()

# 主函数
if __name__ == '__main__':
    main()