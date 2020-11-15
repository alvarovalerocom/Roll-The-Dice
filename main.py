import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QLabel)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSlot
import random
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        btn = QPushButton('Press me', self)
        btn.setToolTip("Press to roll the dice")
        btn.resize(btn.sizeHint())
        btn.move(150, 300)
        btn.clicked.connect(self.on_clicked)
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Roll the dice app')
        self.number1 = QLabel(self)
        self.number1.setText("0")
        self.number1.move(140,100)
        
        self.number2 = QLabel(self)
        self.number2.setText("0")
        self.number2.move(250,100)
        
        self.show()
    @pyqtSlot()
    def on_clicked(self):
        a = random.randint(1,6)
        b = random.randint(1,6)
        a = str(a)
        b = str(b)
        self.number1.setText(a)
        self.number1.adjustSize()
        self.number2.setText(b)
        self.number2.adjustSize()
        
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
