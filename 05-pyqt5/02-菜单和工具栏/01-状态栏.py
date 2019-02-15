import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Example(QMainWindow):
    """
    注意这里继承的是QMainWindow
    """
    def __init__(self):
        super().__init__()

        self.statusBar().showMessage('Ready')

        self.resize(480, 360)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

