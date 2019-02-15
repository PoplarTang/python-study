from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import sys

app = QApplication(sys.argv)

w = QWidget()

w.setGeometry(800, 200, 480,320)
w.setWindowIcon(QIcon("图片7.gif"))
w.setWindowTitle("标题")
w.show()

sys.exit(app.exec_())
