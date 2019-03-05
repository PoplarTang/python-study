import time
import threading
"""线程的基本使用"""
def say():
    print("北京第三区交通委提醒您")
    time.sleep(1)


def main_in_thread():
    for i in range(5):
        thread = threading.Thread(target=say)
        thread.start()



def main():
    for i in range(5):
        say()

if __name__ == '__main__':
    # main()
    main_in_thread()
