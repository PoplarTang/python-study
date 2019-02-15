import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(480, 360)
        # self.move(0,0)
        self.center()
        self.show()

    def center(self):
        fg = self.frameGeometry()
        # QtGui.QDesktopWidget提供了用户的桌面信息，包括屏幕的大小。
        cp = QDesktopWidget().availableGeometry().center()
        print(cp) # PyQt5.QtCore.QPoint(959, 524)

        fg.moveCenter(cp)
        print(fg) # PyQt5.QtCore.QRect(720, 345, 479, 359)
        self.move(fg.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

