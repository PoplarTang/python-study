import sys
from PyQt5.QtWidgets import (QApplication,qApp, QAction, QMainWindow, QMenu)
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    """
    注意这里继承的是QMainWindow
    """
    def __init__(self):
        super().__init__()

        menubar = self.menuBar()

        fileMenu = menubar.addMenu("File")

        # 子菜单
        impMenu = QMenu("Import", self)
        impMenu.addAction(QAction("Import mail", self))
        impMenu.addAction(QAction("Import text", self))
        impMenu.addAction(QAction("Import html", self))

        fileMenu.addAction(QAction("New", self))
        fileMenu.addMenu(impMenu)
        # 退出Action
        fileMenu.addAction(self.exit_action())

        # 打开状态栏
        bar = self.statusBar()
        bar.showMessage("Ready")

        self.resize(480, 360)
        self.setWindowIcon(QIcon('exit.jpg'))
        self.setWindowTitle("Simple Menu")
        self.show()

    def exit_action(self):
        exitAct = QAction(QIcon('exit.jpg'), "Exit", self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        return exitAct


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

