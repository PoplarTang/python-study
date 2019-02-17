import sys
from PyQt5.QtWidgets import (QApplication, qApp, QAction, QMainWindow, QMenu)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    """
    注意这里继承的是QMainWindow
    """

    def __init__(self):
        super().__init__()

        self.resize(480, 360)
        self.setWindowIcon(QIcon('exit.jpg'))
        self.setWindowTitle("Example")
        self.show()

    def contextMenuEvent(self, event):
        cmenu = QMenu()
        newAct = cmenu.addAction("New")
        openAct = cmenu.addAction("Open")
        copyAct = cmenu.addAction("Copy")
        quitAct = cmenu.addAction("Quit")
        to_global = self.mapToGlobal(event.pos())
        print(to_global)
        action = cmenu.exec_(to_global)

        if action == quitAct:
            qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
