import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        self.button = QPushButton("確認")
        self.button.clicked.connect(self.clickCallBack)
        self.button.is_clicked = False
        
        self.label = QLabel()
        self.label.setFont(QFont("MS UI Gothic", 12, QFont.Black))
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.layout = QGridLayout()
        self.layout.addWidget(self.button, 0, 0)
        self.layout.addWidget(self.label, 1, 0)
        
        self.setLayout(self.layout)
        self.show()
        
    def clickCallBack(self):
        if self.button.is_clicked is False:
            self.label.setText("Python課題")
            self.button.is_clicked = True
        else:
            self.label.setText("確認済み")

app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())