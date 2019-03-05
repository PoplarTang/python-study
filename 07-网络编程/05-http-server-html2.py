from socket import *
import re

def handle_request(client):
    """ 响应客户端请求的核心函数 """
    request_data = client.recv(1024)
    # 判断客户端是否已经断开链接
    if not request_data:
        print("客户端已经断开连接！")
        # 关闭当前连接
        client.close()
        # 退出，代码不再向后执行
        return

    # 目的：得到 客户端 请求行
    # 对客户端请求的数据进行分析
    req_str = request_data.decode()

    # 根据”\r\n“ 分割请求头
    # 得到存储每行请求数据的列表
    req_list = req_str.split("\r\n")

    # 使用正则 取出 请求头中的 路径部分
    ret = re.search(r"\s(.*)\s", req_list[0])
    if not ret:
        print("用户请求报文格式错误!")
        client.close()
        return

    # 得到路径
    path_info = ret.group(1)
    print("接收到用户请求：", path_info)
    if path_info == "/":
        path_info = "/index.html"

    resp_header = "Server:Python-Web1.0\r\n"
    blank = "\r\n"

    try:
        # 读取指定路径文件，并且返回
        with open("static"+path_info, "rb") as file:
            # 读取文件的二进制数据
            resp_content = file.read()

    except Exception as e:
        # 开始拼接响应数据
        resp_line = "HTTP/1.1 404 Not Found\r\n"
        resp_content = "Error !!! %s" % str(e)
        resp_content = resp_content.encode()
    else:
        # 开始拼接响应数据
        resp_line = "HTTP/1.1 200 OK\r\n"

    # 拼接响应头
    resp_data = (resp_line + resp_header + blank).encode()
    resp_data += resp_content

    # 发送数据
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
