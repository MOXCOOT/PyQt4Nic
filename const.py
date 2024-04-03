from PyQt5.QtGui import *

LRratio = {"left": 2, "right": 3}

DEFULT_KEY = "dada"
DEFULT_BLOCK_SIZE = "134479872"
DEFULT_BLOCK_NUMBER = "40"
DEFULT_FONT_SIZE = 10
DEFULT_FONT_FAMILY = "Courier"
DEFULT_WINDOWTITLE = "Receiver"
DEFULT_WINDOW_SIZE = {"width": 1000, "height": 618}

font = QFont()
font.setFamily(DEFULT_FONT_FAMILY)  # 设置字体家族
font.setPointSize(DEFULT_FONT_SIZE)  # 设置字体大小


def update_text(self, edit):
    # old_pos = edit.textCursor().position()
    # 创建一个 QTextCursor
    text_cursor = edit.textCursor()
    # # 移动 cursor 到文本末尡
    # text_cursor.movePosition(QTextCursor.End)
    # 获取滚动条的当前位置和最大位置
    scrollbar = edit.verticalScrollBar()
    print(scrollbar.maximum() - scrollbar.value())
    at_bottom = scrollbar.maximum() - scrollbar.value() < 10
    # # 设置 textEdit 的 cursor 为刚刚移动的 cursor
    # edit.setTextCursor(text_cursor)

    # 读取输出并添加到文本编辑区域
    text = self.process.readAllStandardOutput().data().decode()[:-1]
    edit.append(text)
    # edit.insertPlainText(text)
    # 如果滚动条原本就在底部，那么保持在底部

    # text_cursor = edit.textCursor()
    # text_cursor.setPosition(old_pos)
    # edit.setTextCursor(text_cursor)

    # print(at_bottom)

    if at_bottom:
        print("at——bottom")
        text_cursor.movePosition(QTextCursor.End)
        edit.setTextCursor(text_cursor)
        # edit.ensureCursorVisible()

    print(text)


# def update_text(self, edit):
#     # 创建一个 QTextCursor
#     text_cursor = edit.textCursor()
#     # 移动 cursor 到文本末尾
#     text_cursor.movePosition(QTextCursor.End)
#     # 设置 textEdit 的 cursor 为刚刚移动的 cursor
#     edit.setTextCursor(text_cursor)
#     # 读取输出并添加到文本编辑区域
#     text = self.process.readAllStandardOutput().data().decode()
#     edit.insertPlainText(text)

#     print(text)


def on_process_started():
    print("Process has started successfully.")
