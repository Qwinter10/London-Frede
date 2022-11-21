from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import choice


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('paint.ui', self)
        self.qp = QPainter()
        self.pushButton.clicked.connect(self.paintEvent)

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.painting()
        self.qp.end()

    def painting(self):
        self.qp.setBrush(QColor(255, 255, 127))
        self.qp.drawEllipse(20, 20, choice(range(0, 255)), choice(range(0, 255)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
