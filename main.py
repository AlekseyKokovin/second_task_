import sys
from random import randrange

from PyQt5.QtCore import QRect
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 379)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(221, 0, 111, 28))
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        font = QtGui.QFont()
        font.setPointSize(24)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Нажми меня"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False

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
        radius = randrange(1, 250)
        qp.setPen(QColor(randrange(255), randrange(255), randrange(255)))
        qp.drawEllipse(QRect(0, 50, radius, radius))
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

