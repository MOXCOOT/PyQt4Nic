import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from const import *
from main import MainApp


class PsrdadaApp(QWidget):
    text = ""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI(parent)

    def initUI(self, par):
        self.setWindowTitle("MyApp")
        self.resize(300, 300)

        vbox = QVBoxLayout()

        HBOX = QHBoxLayout()

        vIbox1 = QVBoxLayout()
        label1 = QLabel("key:", self)
        label2 = QLabel("size of block:", self)
        label3 = QLabel("number of block:", self)
        vIbox1.addWidget(label1)
        vIbox1.addWidget(label2)
        vIbox1.addWidget(label3)

        vIbox2 = QVBoxLayout()
        self.textEdit1 = QLineEdit(self)
        self.textEdit2 = QLineEdit(self)
        self.textEdit3 = QLineEdit(self)
        vIbox2.addWidget(self.textEdit1)
        vIbox2.addWidget(self.textEdit2)
        vIbox2.addWidget(self.textEdit3)

        self.textEdit1.setPlaceholderText(DEFULT_KEY)
        self.textEdit2.setPlaceholderText(DEFULT_BLOCK_SIZE)
        self.textEdit3.setPlaceholderText(DEFULT_BLOCK_NUMBER)

        HBOX.addLayout(vIbox1)
        HBOX.addLayout(vIbox2)
        HBOX.setStretch(0, 2)
        HBOX.setStretch(1, 3)
        vbox.addLayout(HBOX)

        hIbox1 = QHBoxLayout()
        hIbox2 = QHBoxLayout()

        self.btn = QPushButton("create buffer", self)
        self.btn.clicked.connect(lambda: self.on_click(1))
        hIbox1.addWidget(self.btn)

        self.btn = QPushButton("clear buffer", self)
        self.btn.clicked.connect(lambda: self.on_click(0))
        hIbox1.addWidget(self.btn)

        self.btn = QPushButton("delete buffer", self)
        self.btn.clicked.connect(lambda: self.on_click(2))
        hIbox2.addWidget(self.btn)

        self.btn = QPushButton("monitor buffer", self)
        self.btn.clicked.connect(lambda: self.on_click(3))
        hIbox2.addWidget(self.btn)

        vbox.addLayout(hIbox1)
        vbox.addLayout(hIbox2)

        self.setLayout(vbox)

        # 创建一个QProcess对象
        self.process = QProcess(self)
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        # self.process.errorOccurred.connect(self.handle_error)
        self.process.started.connect(on_process_started)
        # 连接其输出信号到update_text方法
        self.process.readyReadStandardOutput.connect(
            lambda: update_text(self, par.textEdit2)
        )
        # # 运行ping命令
        # self.process.start('ping www.baidu.com')

    def on_click(self, flag):
        KEY = self.textEdit1.text() if self.textEdit1.text() != "" else DEFULT_KEY
        B = self.textEdit2.text() if self.textEdit2.text() != "" else DEFULT_BLOCK_SIZE
        N = (
            self.textEdit3.text()
            if self.textEdit3.text() != ""
            else DEFULT_BLOCK_NUMBER
        )
        if flag == 1:
            self.process.start("dada_db", ["-k", KEY, "-n", N, "-b", B])
        elif flag == 2:
            self.process.start("dada_db", ["-k", KEY, "-d"])
        elif flag == 3:
            self.process.start("dada_dbmonitor", ["-k", KEY])
        else:
            self.process.kill()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = PsrdadaApp()
    ex.show()
    sys.exit(app.exec_())
