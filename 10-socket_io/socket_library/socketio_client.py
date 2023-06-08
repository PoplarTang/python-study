import socketio
import threading

from eventlet import Queue

CALLBACK_MESSAGE = 0
CALLBACK_DISCONNECT = -1
CALLBACK_CONNECTED = 1


class SocketIOClientThread(threading.Thread):
    def __init__(self, url, message_callback=None):
        threading.Thread.__init__(self, daemon=True)
        self.sio = socketio.Client()
        self.url = url
        self.message_queue = Queue()
        self.message_callback = message_callback
        self.is_connected = False

    def on_connect(self):
        print('已连接到服务器')
        self.is_connected = True
        if self.message_callback:
            self.message_callback(CALLBACK_CONNECTED, None)

    def on_disconnect(self):
        print('已断开与服务器的连接')
        self.is_connected = False
        if self.message_callback:
            self.message_callback(CALLBACK_DISCONNECT, None)

    def handle_message(self, data):
        print('收到消息:', data)
        self.message_queue.put(data)
        # if self.message_callback:
        #     self.message_callback(CALLBACK_MESSAGE, data)

    def send_message(self, message):
        if self.is_connected:
            self.sio.emit('message', message)

    def get_message(self):
        if not self.message_queue.empty():
            return self.message_queue.get()
        return None

    def run(self):
        self.sio.on('connect')(self.on_connect)
        self.sio.on('disconnect')(self.on_disconnect)
        self.sio.on('message')(self.handle_message)
        self.sio.connect(self.url)
        self.sio.wait()


class SocketIOClient:
    def __init__(self):
        self.sio = socketio.Client()

    def on_connect(self):
        print('已连接到服务器')

        # 向服务器发送消息
        self.send_message('Hello, Server!')

    def on_disconnect(self):
        print('已断开与服务器的连接')

    def handle_message(self, data):
        print('收到消息:', data)

    # 连接到服务器
    def connect(self, url):
        self.sio.on('connect')(self.on_connect)
        self.sio.on('disconnect')(self.on_disconnect)
        self.sio.on('message')(self.handle_message)

        self.sio.connect(url)

    # 发送消息给服务器
    def send_message(self, message):
        self.sio.emit('message', message)

    # 开始事件循环
    def start(self):
        self.sio.wait()


if __name__ == '__main__':
    client = SocketIOClient()
    client.connect('http://localhost:5000')
    client.start()
