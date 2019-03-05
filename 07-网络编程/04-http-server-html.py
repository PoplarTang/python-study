from socket import *

def handle_request(client):
    # 接收客户端请求
    req_data = client.recv(1024)
    if not req_data:
        print("客户端已断开连接！")
        client.close()
        return # 退出，后边代码不再执行

    # 准备响应报文
    resp_line="HTTP/1.1 200 OK\r\n"
    resp_header="Server: Python-Web1.0\r\n"
    blank = "\r\n"
    # resp_content = "HelloWorld!"
    resp_data = resp_line + \
                resp_header + \
                blank

    # 读取指定路径文件，并且返回
    with open("static/index.html", "rb") as f:
        # 读取文件的二进制数据
        resp_content = f.read()

    resp_data = resp_data.encode() + resp_content

    # 回复数据
    client.send(resp_data)
    # 关闭socket
    client.close()


# 启动TCP服务器
def main():
    # 创建套接字
    tcp_server=socket(AF_INET, SOCK_STREAM)
    # 设置地址重用
    tcp_server.setsockopt(SOL_SOCKET,
                          SO_REUSEADDR, True)
    # 绑定IP和端口
    tcp_server.bind(("", 8080))
    # 设置套接字为被动，接收客户端连接
    tcp_server.listen(128)
    while True:
        # 得到接入的客户端，IP和端口
        client, ip_port = tcp_server.accept()
        print("[新客户端上线]", ip_port)
        # 响应客户端请求
        handle_request(client)

if __name__ == '__main__':
    main()
