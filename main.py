import sys

from random import randint as rnd
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPainter



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('1.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_ellipse(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        r = rnd(1, 301)
        qp.drawEllipse(rnd(1, 800), rnd(1,600), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
