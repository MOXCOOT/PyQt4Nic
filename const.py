from PyQt5.QtGui import *

LRratio = {"left": 2, "right": 3}

DEFULT_KEY = "dada"
DEFULT_BLOCK_SIZE = "134479872"
DEFULT_BLOCK_NUMBER = "40"
DEFULT_FONT_SIZE = 10
DEFULT_FONT_FAMILY = "Monospace"
DEFULT_WINDOWTITLE = "Receiver"
DEFULT_WINDOW_SIZE = {"width": 1000, "height": 618}
DEFULT_IS_BOLD = False

font = QFont()
font.setFamily(DEFULT_FONT_FAMILY)  # 设置字体家族
font.setPointSize(DEFULT_FONT_SIZE)  # 设置字体大小
font.setBold(DEFULT_IS_BOLD)


def update_text(self, edit):
    # 创建一个 QTextCursor
    text_cursor = edit.textCursor()
    # 获取滚动条的当前位置和最大位置
    scrollbar = edit.verticalScrollBar()
    # print(scrollbar.maximum() - scrollbar.value())
    at_bottom = scrollbar.maximum() - scrollbar.value() < 10
    # 读取输出并添加到文本编辑区域
    text = self.process.readAllStandardOutput().data().decode()[:-1]
    edit.append(text)
    if at_bottom:
        # print("at——bottom")
        text_cursor.movePosition(QTextCursor.End)
        edit.setTextCursor(text_cursor)
        # edit.ensureCursorVisible()
    print(text)


def on_process_started():
    print("Process has started successfully.")
