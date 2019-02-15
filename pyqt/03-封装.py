from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import sys

app = QApplication(sys.argv)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 200, 480,320)
        self.setWindowIcon(QIcon("图片7.gif"))
        self.setWindowTitle("标题")
        self.show()

e = Example()

sys.exit(app.exec_())
