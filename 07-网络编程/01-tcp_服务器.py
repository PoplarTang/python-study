from socket import *

# 创建socket

s_socket = socket(AF_INET, SOCK_STREAM)

# 绑定本地信息

s_socket.bind(("", 7788))

# 准备接收连接，参数为等待队列数

s_socket.listen(128)

# 阻塞执行：获取新客户端socket、IP、端口号

c_socket, ip_port = s_socket.accept()
print("有新的客户端：",ip_port)

# 接受客户端发来的数据

r_data = c_socket.recv(1024)
print('收到数据: ', r_data.decode("gbk"))

# 回复数据给客户端

c_socket.send('消息收到！'.encode())

# 关闭这个客户端

c_socket.close()
