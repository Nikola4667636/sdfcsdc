import io
import sys

from random import randint as rnd
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPainter


class MakeForm:
    def __init__(self, form):
        self.form = form

    def get_form(self):
        return self.form


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(form.get_form())
        uic.loadUi(f, self)
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
        red, g, b = rnd(1, 255), rnd(1, 255), rnd(1, 255)
        qp.setBrush(QColor(red, g, b))
        r = rnd(1, 301)
        qp.drawEllipse(rnd(1, 800), rnd(1,600), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>151</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string>Создать окружность</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>"""

    form = MakeForm(template)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
