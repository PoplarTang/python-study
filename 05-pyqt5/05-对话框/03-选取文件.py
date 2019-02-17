from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QTextEdit, QFileDialog, QAction)

from PyQt5.QtGui import QIcon
import sys


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon("file.jpg"), "Open", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("Open new file")
        openFile.triggered.connect(self.showDialog)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(openFile)

        self.setGeometry(300, 300, 480, 360)
        self.setWindowTitle("文件选择对话框")
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self,"打开文件", "/home/ty")
        print(fname, len(fname))
        if fname[0]:
            with open(fname[0], 'r') as f:
                data  = f.read()
                self.textEdit.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
