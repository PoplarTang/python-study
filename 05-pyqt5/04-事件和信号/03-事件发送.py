from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QHBoxLayout,QPushButton)
import sys


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def btnClicked(self):
        sender = self.sender()
        print(sender)
        self.statusBar().showMessage(sender.text() + " was pressed")

    def init_ui(self):

        btn1 = QPushButton("确认", self)
        btn2 = QPushButton("取消", self)
        btn1.move(30, 50)
        btn2.move(130, 50)

        btn1.clicked.connect(self.btnClicked)
        btn2.clicked.connect(self.btnClicked)

        self.statusBar()

        self.resize(480,360)
        self.setWindowTitle("信号事件处理")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
