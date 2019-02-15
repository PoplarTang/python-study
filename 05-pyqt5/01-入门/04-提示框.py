import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QMessageBox, QToolTip, QPushButton)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        # QToolTip.setFont(QFont('SansSerif', 12))
        # 创建提示框
        self.setToolTip("This is a <b>QWidget</b>")

        btn = QPushButton('Button', self)
        btn.setToolTip("This is a <b>QPushButton</b> widget")
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        # 测试点击退出
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 80)

        self.setGeometry(300,300, 480,320)
        self.setWindowTitle("测试提示")

        self.show()

    def closeEvent(self, qCloseEvent):
        """
        改变默认关闭时间
        :param qCloseEvent:
        """
        reply = QMessageBox.question(self, "Message",
                                     "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            qCloseEvent.accept()
        else:
            qCloseEvent.ignore()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())
