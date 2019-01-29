def send_msg(msg):
    print("msg [%s] has been sended" % msg)

msg_count = 1

# 可以防止被作为模块导入时, 执行了不必要的代码
if __name__ == "__main__" :
    print("模块自主执行")
    print("当前发送消息数: %d" % msg_count)

