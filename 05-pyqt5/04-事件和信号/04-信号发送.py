from PyQt5.QtWidgets import (QApplication, QWidget,
                             )
from PyQt5.QtCore import QObject, pyqtSignal
import sys

class Communicate(QObject):
    closeApp = pyqtSignal()
    printLog = pyqtSignal()

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        # def ppp(): print("哈哈, 页面要关闭了哦")
        self.c.printLog.connect(lambda : print("嘿嘿, this is a slots"))

        self.init_ui()


    def init_ui(self):
        self.setWindowTitle("信号发送")
        self.show()

    def mousePressEvent(self, QMouseEvent):
        self.c.printLog.emit()
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
