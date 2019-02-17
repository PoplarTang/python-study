from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QHBoxLayout,QVBoxLayout,QPushButton)
import sys

app = QApplication(sys.argv)

w = QWidget()

hbox = QHBoxLayout()
hbox.addStretch(1)
hbox.addWidget(QPushButton("Ok"))
hbox.addWidget(QPushButton("Cancel"))

vbox = QVBoxLayout()
vbox.addStretch(1)
vbox.addLayout(hbox)

w.setLayout(vbox)

w.resize(480,360)
w.setWindowTitle("盒布局")
w.show()

exec_ = app.exec_()
app.exit(exec_)
