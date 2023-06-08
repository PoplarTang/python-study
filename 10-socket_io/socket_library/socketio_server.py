import eventlet
import socketio
import re
from socket_library.models import *

# 正则，用于验证蛇身的格式是否符合类似230,30;220,31;210,30的格式
REGEX_SNAKE_BODY = r'^(\d+,\d+;)*(\d+,\d+)$'

class SocketIOServer:
    def __init__(self):
        self.sio = socketio.Server()
        self.app = socketio.WSGIApp(self.sio)
        self.server_info = {
            "name": "游戏",
            "creator": "小明",
            "version": "1.0.0",
        }
        self.clients = {}

        # 开启定时任务，每隔0.05秒向所有客户端发送消息
        eventlet.spawn(self.send_message_loop)

    def send_message_loop(self):
        """
        定时向所有客户端发送消息
        :return:
        """
        while True:
            # 构建所有客户端的信息
            # 只取出每个client中的body和info
            filtered_client_lst = [
                {k: v for k, v in client.items() if k in ['body', 'info']}
                for client in self.clients.values()
            ]

            game_data = Msg(MsgType.SERVER_GAME_DATA, data=filtered_client_lst).to_dict()
            self.sio.emit('message', game_data)
            eventlet.sleep(0.05)

    def on_connect(self, sid, environ):
        print('客户端连接:', sid)
        self.clients[sid] = {
            'sid': sid,
            # 其他客户端相关信息
            "score": 0,
            "body": "",
            'info': {
                "name": "玩家",
                "color": "#000000",
            }
        }
        resp = Msg(0, '欢迎加入游戏', self.server_info).to_dict()
        self.sio.emit('message', resp, room=sid)

    def on_disconnect(self, sid):
        print('客户端断开连接:', sid)
        if sid in self.clients:
            del self.clients[sid]
        self.sio.emit('message', '玩家离开游戏', room=sid)

    def handle_message(self, sid, data):
        msg = f'玩家 {sid} 说: {data}'
        print('收到消息:', msg)
        # self.sio.emit('message', msg)
        if "code" not in data:
            return
        code = data["code"]

        client = self.clients[sid]
        if code == MsgType.CLIENT_INFO.value:
            # 保存客户端信息
            current_info = client['info']
            filtered_dict = {k: v for k, v in data['data'].items() if k in current_info}
            current_info.update(filtered_dict)
        elif code == MsgType.CLIENT_SNAKE_POSITION.value:
            # 保存蛇的位置信息
            body_data = data['data']
            # 进行格式校验，验证是否符合x,y;x,y;x,y...的格式
            if not isinstance(body_data, str):
                return
            body_data = body_data.strip()
            if not body_data:
                return
            # 使用正则表达式进行验证
            pattern = re.compile(REGEX_SNAKE_BODY)
            if not pattern.match(body_data):
                return
            client['body'] = body_data

    # 启动服务器
    def run(self, host, port):
        self.sio.on('connect')(self.on_connect)
        self.sio.on('disconnect')(self.on_disconnect)
        self.sio.on('message')(self.handle_message)

        eventlet.wsgi.server(eventlet.listen((host, port)), self.app)

    # 发送消息给指定客户端
    def send_message_to_client(self, client_sid, message):
        if client_sid in self.clients:
            self.sio.emit('message', message, room=client_sid)

    def set_server_info(self, info):
        self.server_info = info


if __name__ == '__main__':
    # 使用 eventlet 启动服务器
    io_server = SocketIOServer()
    io_server.set_server_info({
        "name": "贪吃蛇游戏",
        "creator": "小明",
        "version": "1.0.0",
    })
    io_server.run(host='0.0.0.0', port=5000)
