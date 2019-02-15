from PyQt5.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)

w = QWidget()
# 设置大小
w.resize(480,360)
# 设置左上角坐标
w.move(900, 200)
w.setWindowTitle("标题")
w.show()

sys.exit(app.exec_())
