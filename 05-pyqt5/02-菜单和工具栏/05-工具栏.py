import sys
from PyQt5.QtWidgets import (
    QApplication,qApp, QAction, QMainWindow, QMenu,
    QTextEdit
)
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    """
    注意这里继承的是QMainWindow
    """
    def __init__(self):
        super().__init__()
        # 文本编辑区域
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)


        # 子菜单
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")

        impMenu = QMenu("Import", self)
        impMenu.addAction(QAction("Import mail", self))
        impMenu.addAction(QAction("Import text", self))
        impMenu.addAction(QAction("Import html", self))

        fileMenu.addAction(QAction("New", self))
        fileMenu.addMenu(impMenu)


        # 工具栏
        exitAct = QAction(QIcon("exit.jpg"), "exit", self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setStatusTip("Exit app")
        exitAct.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar("Main Tool Bar")
        self.toolbar.addAction(QAction(QIcon("img/back.png"), "back", self))
        self.toolbar.addAction(QAction(QIcon("img/forward.png"), "forward", self))
        self.toolbar.addAction(exitAct)

        # 打开状态栏
        bar = self.statusBar()
        bar.showMessage("Ready")

        self.resize(480, 360)
        self.setWindowIcon(QIcon('exit.jpg'))
        self.setWindowTitle("Simple Menu")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

