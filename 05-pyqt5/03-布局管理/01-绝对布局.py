from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import sys

app = QApplication(sys.argv)

print("-----------1")
w = QWidget()
label1 = QLabel("Haha", w)
label1.move(10, 10)

label2 = QLabel("gaga", w)
label2.move(30, 40)

label3 = QLabel("heihei", w)
label3.move(50, 60)

w.resize(200,100)
w.setWindowTitle("绝对布局")
w.show()

print("-----------2")
exec_ = app.exec_()
app.exit(exec_)
print("-----------3", exec_)
