from PyQt5.QtWidgets import (QApplication, QWidget,
                             QLabel, QGridLayout,QVBoxLayout)

from PyQt5.QtCore import Qt
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        grid = QGridLayout()
        grid.setSpacing(10)

        self.label = QLabel("x: {0},  y: {1}".format(0, 0))
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)

        self.setLayout(grid)


        self.resize(480,360)
        self.setWindowTitle("鼠标事件对象")
        self.show()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()
        self.label.setText("x: {0},y: {1}".format(x, y))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
