import socket

# 创建TCP连接
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# DNS解析 和  连接HTTP服务器
tcp_socket.connect(("www.itcastcpp.cn", 80))

# 组包 发送HTTP请求报文

# 请求行
request_line = "GET / HTTP/1.1\r\n"

# 请求头
request_header = "Host: www.itcastcpp.cn\r\n"
request_data = request_line + request_header + "\r\n"

# 发送请求
tcp_socket.send(request_data.encode())


# 接收响应报文
response_data = tcp_socket.recv(4096)

# 对响应报文进行解析 -- 切割
response_str_data = response_data.decode()
# print(response_data)

# '\r\n\r\n'之后的数据就是响应体数据
index = response_str_data.find("\r\n\r\n")

# 切割出的数据就是文件数据
html_data = response_str_data[index+4:]

# data_file = open("index.html", "wb")
# data_file.write(html_data.encode())
# data_file.close()
with open("index.html", "wb") as file:
    file.write(html_data.encode())

# 关闭套接字
tcp_socket.close()
