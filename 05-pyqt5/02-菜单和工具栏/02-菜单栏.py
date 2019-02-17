import sys
from PyQt5.QtWidgets import QApplication,qApp, QAction, QMainWindow
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    """
    注意这里继承的是QMainWindow
    """
    def __init__(self):
        super().__init__()

        menubar = self.menuBar()

        exitAct = QAction(QIcon('exit.jpg'),"Exit", self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        fileMenu = menubar.addMenu("File")
        fileMenu.addAction(exitAct)

        # 打开状态栏
        bar = self.statusBar()

        self.resize(480, 360)
        self.setWindowIcon(QIcon('exit.jpg'))
        self.setWindowTitle("Simple Menu")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

