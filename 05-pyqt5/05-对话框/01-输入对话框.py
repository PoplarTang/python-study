from PyQt5.QtWidgets import (QApplication, QWidget,
                    QPushButton, QInputDialog, QLineEdit)
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.btn = QPushButton("对话框",self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("信号事件处理")
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, "输入对话框", "请输入姓名:")

        if ok:
            self.le.setText(str(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
