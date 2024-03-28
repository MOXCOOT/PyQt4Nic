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
        self.textEdit = QTextEdit()

        self.textEdit.setReadOnly(True)
        
        splitterIn = QSplitter(Qt.Vertical)
        splitterIn.addWidget(myApp)
        splitterIn.addWidget(self.textEdit) 
        # myApp.setMinimumHeight(100)
        splitterIn.setSizes([100, 300])


        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(splitterIn)
        splitter.addWidget(self.psrdadaApp)
        splitter.setSizes([300, 100])

        hbox = QHBoxLayout(self)

        # hbox.addWidget(splitterIn)
        # hbox.addWidget(psrdadaApp)
        
        hbox.addWidget(splitter)

        self.setLayout(hbox)
        self.setWindowTitle('Receiver')
        self.center()
        self.resize(800,400)


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

