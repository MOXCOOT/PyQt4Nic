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
        self.myApp = MyApp(self)
        self.textEdit1 = QTextEdit()
        self.textEdit2 = QTextEdit()

        self.textEdit1.setFont(font)  # 应用字体到文本框
        self.textEdit2.setFont(font)
        self.textEdit1.setReadOnly(True)
        self.textEdit2.setReadOnly(True)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.myApp)
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
        self.setWindowTitle(DEFULT_WINDOWTITLE)
        self.center()
        self.resize(DEFULT_WINDOW_SIZE["width"], DEFULT_WINDOW_SIZE["height"])

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
