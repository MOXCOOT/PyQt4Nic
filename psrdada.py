import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from main import MainApp

class PsrdadaApp(QWidget):

    text=""
    def __init__(self,parent=None):
        super().__init__(parent)
        # print(type(parent))
        self.initUI(parent)

    def initUI(self,par):
        self.setWindowTitle('MyApp') 
        self.resize(300, 300)

        vbox = QVBoxLayout()

        # 创建三个文本框并添加到布局中
        hbox1 = QHBoxLayout()
        label1 = QLabel('key:', self)
        self.textEdit1 = QLineEdit(self)
        hbox1.addWidget(label1)
        hbox1.addWidget(self.textEdit1)
        vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout()
        label2 = QLabel('size of block:', self)
        self.textEdit2 = QLineEdit(self)
        hbox2.addWidget(label2)
        hbox2.addWidget(self.textEdit2)
        vbox.addLayout(hbox2)

        hbox3 = QHBoxLayout()
        label3 = QLabel('number of block:', self)
        self.textEdit3 = QLineEdit(self)
        hbox3.addWidget(label3)
        hbox3.addWidget(self.textEdit3)
        vbox.addLayout(hbox3)

        # 创建一个按钮并添加到布局中
        self.btn = QPushButton('create buffer', self)
        self.btn.clicked.connect(self.on_click)
        vbox.addWidget(self.btn)
        # 创建一个按钮并添加到布局中
        self.btn = QPushButton('clear buffer', self)
        self.btn.clicked.connect(self.on_click)
        vbox.addWidget(self.btn)
        # 创建一个按钮并添加到布局中
        self.btn = QPushButton('delete buffer', self)
        self.btn.clicked.connect(lambda:self.on_click(1))
        vbox.addWidget(self.btn)
        # 创建一个按钮并添加到布局中
        self.btn = QPushButton('monitor buffer', self)
        self.btn.clicked.connect(lambda:self.on_click(0))
        vbox.addWidget(self.btn)

        self.setLayout(vbox)
        # 创建一个QProcess对象
        self.process = QProcess(self)
        # 连接其输出信号到update_text方法
        self.process.readyReadStandardOutput.connect(lambda:self.update_text(par))
        # # 运行ping命令
        # self.process.start('ping www.baidu.com')

    def on_click(self,flag):
        if flag == 0:
            self.process.start('ping www.baidu.com')
        else:
            self.process.kill()
        # print(f'Texts are: {self.textEdit1.text()}, {self.textEdit2.text()}, and {self.textEdit3.text()}')
            
    def update_text(self,par):
        # 读取输出并添加到文本编辑区域
        text = self.process.readAllStandardOutput().data().decode()
        par.textEdit.append(text)
        print(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PsrdadaApp()
    ex.show()
    sys.exit(app.exec_())
