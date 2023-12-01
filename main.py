import sys
from random import randrange

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, a0):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.run2(qp)
            qp.end()

    def run2(self, qp):
        radius = randrange(1, 500)
        qp.setPen(QColor(255, 255, 0))
        qp.drawEllipse(QRect(0, 50, radius, radius))
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
