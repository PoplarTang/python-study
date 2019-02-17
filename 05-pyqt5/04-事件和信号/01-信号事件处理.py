from PyQt5.QtWidgets import (QApplication, QWidget,
             QLCDNumber, QSlider, QVBoxLayout)

from PyQt5.QtCore import Qt
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def handleChange(self, value):
        print(value, type(value))
        self.lcd.display(value)

    def init_ui(self):

        self.lcd = QLCDNumber()
        slider = QSlider(Qt.Horizontal)
        slider.valueChanged.connect(self.handleChange)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)
        self.resize(250,150)
        self.setWindowTitle("信号事件处理")
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
