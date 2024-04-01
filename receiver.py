from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from psrdada import *
from const import *


class MyApp(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI(parent)

    def initUI(self, par):
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

        self.btn = QPushButton("confirm", self)
        self.btn.clicked.connect(self.on_click)

        vbox.addWidget(self.btn)

        self.setLayout(vbox)

        # 创建一个QProcess对象
        self.process = QProcess(self)
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        # self.process.errorOccurred.connect(self.handle_error)
        self.process.started.connect(on_process_started)
        # 连接其输出信号到update_text方法
        self.process.readyReadStandardOutput.connect(
            lambda: update_text(self, par.textEdit1)
        )

    def on_click(self):
        self.process.start(
            "sudo ./build/udpdadav2 -c 1 --socket-mem 128 --proc-type auto --file-prefix pg1 -w 84:00.1 -- -p 1 -k dada -T 524288"
        )
        # self.process.start("tree")
        # print(
        #     f"Selected items are: {self.combo1.currentText()} and {self.combo2.currentText()}"
        # )
