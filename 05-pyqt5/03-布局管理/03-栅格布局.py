from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QPushButton, QGridLayout)
import sys

app = QApplication(sys.argv)

w = QWidget()

grid = QGridLayout()
w.setLayout(grid)

names = [
    "Cls", "Bck", "", "Close",
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
]
positions = [(i, j) for i in range(5) for j in range(4)]

for pos, name in zip(positions, names):
    if name == "":
        continue
    grid.addWidget(QPushButton(name), *pos)

# w.resize(480,360)
w.setWindowTitle("栅格布局")
w.show()

exec_ = app.exec_()
app.exit(exec_)
