from functools import wraps


class logit(object):
    """
    这个实现有一个附加优势，在于比嵌套函数的方式更加整洁，而且包裹一个函数还是使用跟以前一样的语法：
    @logit('out.log')
    """
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify(func.__name__, *args, **kwargs)
            return func(*args, **kwargs)

        return wrapped_function

    def notify(self, func_name, *args, **kwargs):
        # logit只打日志，不做别的
        pass


class email_logit(logit):
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''

    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self, func_name, *args, **kwargs):
        # 发送一封email到self.email
        # 这里就不做实现了
        print('Sending email to {}, args: {}'.format(self.email, args))

@logit()
def myfunc1():
    pass

@email_logit()
def myfunc2(a, b):
    pass


if __name__ == '__main__':
    myfunc1()
    myfunc2(123, "haha")
