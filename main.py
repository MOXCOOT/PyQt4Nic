import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from psrdada import *
from receiver import *



class MainApp(QWidget):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super(MainApp, cls).__new__(cls, *args, **kwargs)
        return cls._instance


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
        hbox1.setStretch(0, 2)  # psrdadaApp占据3/4的空间
        hbox1.setStretch(1, 3)  # myApp占据1/4的空间

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.textEdit1)
        hbox2.addWidget(self.textEdit2)
        hbox2.setStretch(0, 2)  # psrdadaApp占据3/4的空间
        hbox2.setStretch(1, 3)  # myApp占据1/4的空间

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)
        self.setWindowTitle('Receiver')
        self.center()
        self.resize(1000,618)




        
        # splitterIn = QSplitter(Qt.Vertical)
        # splitterIn.addWidget(myApp)
        # splitterIn.addWidget(self.textEdit2) 
        # # myApp.setMinimumHeight(100)
        # splitterIn.setSizes([100, 300])

        # splitterR = QSplitter(Qt.Vertical)
        # splitterR.addWidget(self.psrdadaApp)
        # splitterR.addWidget(self.textEdit1) 
        # splitterR.setSizes([100, 300])



        # splitter = QSplitter(Qt.Horizontal)
        # splitter.addWidget(splitterR)
        # splitter.addWidget(splitterIn)
        # splitter.setSizes([300, 100])

        # hbox = QHBoxLayout(self)

        # # hbox.addWidget(splitterIn)
        # # hbox.addWidget(psrdadaApp)
        
        # hbox.addWidget(splitter)

        # self.setLayout(hbox)
        # self.setWindowTitle('Receiver')
        # self.center()
        # self.resize(1000,618)


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec_())

