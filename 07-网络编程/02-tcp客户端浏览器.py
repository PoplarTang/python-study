from socket import *
# 创建TCP socket对象
tcp_socket = socket(AF_INET, SOCK_STREAM)
# DNS解析 & 连接HTTP服务器
tcp_socket.connect(("www.itheima.com", 80))
# 准备HTTP请求报文 & 发送
line = "\r\n"

req_line= "GET / HTTP/1.1%s" % line
req_header= "Host: www.itheima.com%s" % line
request_data=req_line+req_header + line
tcp_socket.send(request_data.encode())
# 接收响应报文
resp_data = tcp_socket.recv(4096)
# 解码响应报文
resp_str = resp_data.decode()
# '\r\n\r\n'之后的数据就是响应体数据
index = resp_str.find(line * 2)
# 切割出的数据就是文件数据
html_data = resp_str[index+4:]
# 打开文件，并以二进制型式写入
with open("index.html", "wb") as f:
    f.write(html_data.encode())
# 关闭TCP socket
tcp_socket.close()

