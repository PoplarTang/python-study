import enum


class MsgType(enum.Enum):
    SERVER_ERROR = -1
    SERVER_SUCCESS = 0
    SERVER_GAME_DATA = 1

    CLIENT_INFO = 100
    CLIENT_SNAKE_POSITION = 101


class Msg:
    def __init__(self, code=0, msg='', data=None):
        # 如果code是枚举类型，转换成枚举的value
        if isinstance(code, enum.Enum):
            code = code.value

        self.code = code
        self.msg = msg
        self.data = data

    def to_dict(self):
        return {
            'code': self.code,
            'msg': self.msg,
            'data': self.data,
        }

    def __str__(self):
        return self.to_dict()
