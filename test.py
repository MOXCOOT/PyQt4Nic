import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit
from PyQt5.QtCore import QProcess


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("MyApp")
        self.resize(400, 300)

        vbox = QVBoxLayout()

        # 创建一个文本编辑区域并添加到布局中
        self.textEdit = QTextEdit(self)
        vbox.addWidget(self.textEdit)

        self.setLayout(vbox)

        # 创建一个QProcess对象
        self.process = QProcess(self)
        # 连接其输出信号到update_text方法
        self.process.readyReadStandardOutput.connect(self.update_text)
        # 运行ping命令
        self.process.start("ping www.baidu.com")

    def update_text(self):
        # 读取输出并添加到文本编辑区域
        text = self.process.readAllStandardOutput().data().decode()
        self.textEdit.append(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
