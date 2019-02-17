from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QTextEdit, QLineEdit,
    QPushButton, QGridLayout)
import sys

app = QApplication(sys.argv)

w = QWidget()

grid = QGridLayout()
grid.setSpacing(10)

grid.addWidget(QLabel("Title"), 1, 0)
grid.addWidget(QLineEdit(), 1, 1)

grid.addWidget(QLabel("Author"), 2, 0)
grid.addWidget(QLineEdit(), 2, 1)

grid.addWidget(QLabel("Review"), 3, 0)
grid.addWidget(QTextEdit(), 3, 1, 5, 1)

w.setLayout(grid)
# w.resize(480,360)
w.setWindowTitle("栅格布局")
w.show()

exec_ = app.exec_()
app.exit(exec_)
