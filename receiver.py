from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from psrdada import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # self.setWindowTitle("Receiver Parameters")
        # self.resize(300, 300)

        vbox = QVBoxLayout()

        hbox1 = QHBoxLayout()
        label1 = QLabel("CPU core:", self)
        self.combo1 = QComboBox(self)
        self.combo1.addItems(["1", "2"])
        hbox1.addWidget(label1)
        hbox1.addWidget(self.combo1)
        vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout()
        label2 = QLabel("network port:", self)
        self.combo2 = QComboBox(self)
        self.combo2.addItems(["1", "2"])
        hbox2.addWidget(label2)
        hbox2.addWidget(self.combo2)
        vbox.addLayout(hbox2)

        self.btn = QPushButton("Confirm", self)
        self.btn.clicked.connect(self.on_click)

        vbox.addWidget(self.btn)

        self.setLayout(vbox)

    def on_click(self):
        print(
            f"Selected items are: {self.combo1.currentText()} and {self.combo2.currentText()}"
        )
