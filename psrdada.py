import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

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

        HBOX = QHBoxLayout()

        vIbox1 = QVBoxLayout()
        label1 = QLabel('key:', self)
        label2 = QLabel('size of block:', self)
        label3 = QLabel('number of block:', self)
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


        HBOX.addLayout(vIbox1)
        HBOX.addLayout(vIbox2)
        HBOX.setStretch(0, 2) 
        HBOX.setStretch(1, 3) 
        vbox.addLayout(HBOX)

        # 创建三个文本框并添加到布局中
        # hbox1 = QHBoxLayout()
        # label1 = QLabel('key:', self)
        # self.textEdit1 = QLineEdit(self)
        # hbox1.addWidget(label1)
        # hbox1.addWidget(self.textEdit1)
        # vbox.addLayout(hbox1)

        # hbox2 = QHBoxLayout()
        # label2 = QLabel('size of block:', self)
        # self.textEdit2 = QLineEdit(self)
        # hbox2.addWidget(label2)
        # hbox2.addWidget(self.textEdit2)
        # vbox.addLayout(hbox2)

        # hbox3 = QHBoxLayout()
        # label3 = QLabel('number of block:', self)
        # self.textEdit3 = QLineEdit(self)
        # hbox3.addWidget(label3)
        # hbox3.addWidget(self.textEdit3)
        # vbox.addLayout(hbox3)


        hIbox1 = QHBoxLayout()
        hIbox2 = QHBoxLayout()
        # 创建一个按钮并添加到布局中
        self.btn = QPushButton('create buffer', self)
        self.btn.clicked.connect(lambda:self.on_click(1))
        hIbox1.addWidget(self.btn)
        # 创建一个按钮并添加到布局中
        self.btn = QPushButton('clear buffer', self)
        self.btn.clicked.connect(lambda:self.on_click(1))
        hIbox1.addWidget(self.btn)
        # 创建一个按钮并添加到布局中
        self.btn = QPushButton('delete buffer', self)
        self.btn.clicked.connect(lambda:self.on_click(1))
        hIbox2.addWidget(self.btn)
        # 创建一个按钮并添加到布局中
        self.btn = QPushButton('monitor buffer', self)
        self.btn.clicked.connect(lambda:self.on_click(0))
        hIbox2.addWidget(self.btn)

        vbox.addLayout(hIbox1)
        vbox.addLayout(hIbox2)

        self.setLayout(vbox)
        # 创建一个QProcess对象
        self.process = QProcess(self)
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.errorOccurred.connect(self.handle_error)
        self.process.started.connect(self.on_process_started)



        # 连接其输出信号到update_text方法
        self.process.readyReadStandardOutput.connect(lambda:self.update_text(par))
        # # 运行ping命令
        # self.process.start('ping www.baidu.com')

    def on_click(self,flag):
        if flag == 1:
            # self.process.start('ping baidu.com')
            # self.process.start('dada_dbmonitor')
            self.process.start('dada_dbmonitor',['-k','c1c1'])
            if self.process.state() == QProcess.Running:
                print("Process has started successfully.")
            else:
                print("Failed to start the process.")
            
            # print("sucess pass")
        else:
            self.process.kill()
        # print(f'Texts are: {self.textEdit1.text()}, {self.textEdit2.text()}, and {self.textEdit3.text()}')
            
    def update_text(self,par):
        # 创建一个 QTextCursor
        text_cursor = par.textEdit2.textCursor()

        # 移动 cursor 到文本末尾
        text_cursor.movePosition(QTextCursor.End)

        # 设置 textEdit 的 cursor 为刚刚移动的 cursor
        par.textEdit2.setTextCursor(text_cursor)

        # 读取输出并添加到文本编辑区域
        text = self.process.readAllStandardOutput().data().decode()
        par.textEdit2.insertPlainText(text)

        print(text)

    def handle_error(self, error):
        if error == QProcess.FailedToStart:
            print("Failed to start")
        elif error == QProcess.Crashed:
            print("Process crashed")
        elif error == QProcess.Timedout:
            print("Process timed out")
        elif error == QProcess.WriteError:
            print("Write error")
        elif error == QProcess.ReadError:
            print("Read Error")
        else:
            print("Unknown error")

    def on_process_started(self):
        print("Process has started successfully.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PsrdadaApp()
    ex.show()
    sys.exit(app.exec_())
