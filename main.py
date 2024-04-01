import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from const import *
from psrdada import *
from receiver import *


class MainApp(QWidget):
    def __init__(self):
        super().__init__()

        self.psrdadaApp = PsrdadaApp(self)
        myApp = MyApp()
        self.textEdit1 = QTextEdit()
        self.textEdit2 = QTextEdit()

        font = QFont()
        font.setFamily("Courier")  # 设置字体家族
        font.setPointSize(10)  # 设置字体大小
        self.textEdit1.setFont(font)  # 应用字体到文本框
        self.textEdit2.setFont(font)
        self.textEdit1.setReadOnly(True)
        self.textEdit2.setReadOnly(True)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(myApp)
        hbox1.addWidget(self.psrdadaApp)
        hbox1.setStretch(0, LRratio["left"])
        hbox1.setStretch(1, LRratio["right"])

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.textEdit1)
        hbox2.addWidget(self.textEdit2)
        hbox2.setStretch(0, LRratio["left"])
        hbox2.setStretch(1, LRratio["right"])

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)
        self.setWindowTitle("Receiver")
        self.center()
        self.resize(1000, 618)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec_())
