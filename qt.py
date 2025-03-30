import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QLabel, QFrame, QTextEdit,QPushButton
)
from PyQt6.QtGui import QIcon
# 
# def adjustmargin(layout):
#         layout.setContentsMargins(0, 0, 0, 0)
#         layout.setSpacing(0)
# 
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Sticky Notes")
#         self.setGeometry(100, 100, 400, 400)
#         self.resize(400,400)
#         self.init_ui()
# 
#     def init_ui(self):
# 
#         separator = QFrame()
#         separator.setFrameShape(QFrame.Shape.HLine)
#         separator.setFrameShadow(QFrame.Shadow.Sunken)
# 
#         w = self.width()
#         h = self.height()
#         y = 10
#         btn_h = 30
# 
#         add_btn = QPushButton("✚", self)
#         add_btn.setGeometry(10, y, 30, btn_h)
#   
# 
#         done_btn = QPushButton(self)
#         done_btn.setIcon(QIcon("checkmark.svg"))
#         done_btn.setGeometry(w - 120, y, 50, btn_h)
# 
#         delete_btn = QPushButton(self)
#         delete_btn.setIcon(QIcon("delete.svg"))
#         delete_btn.setGeometry(w - 60, y, 50, btn_h) 
# 
#         text_edit = QTextEdit()
#         text_edit.setStyleSheet("""
#             QTextEdit {
#                 background-color: lightpink;
#                 color: black;
#                 font-family: Consolas, monospace;
#                 font-size: 14px;
#                 border: 1px solid black;
#                 padding: 6px;
#             }
#         """)
# 
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.setStyleSheet("background-color: lightgrey")
#     window.show()
#     sys.exit(app.exec())
# 


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(10,10,400,400)
        self.setMinimumSize(400, 400)
        self.setWindowTitle("Sticky Notes")

        self.add_btn = QPushButton("✚", self)

        self.done_btn = QPushButton(self)
        self.done_btn.setIcon(QIcon("checkmark.svg"))

        self.delete_btn = QPushButton(self)
        self.delete_btn.setIcon(QIcon("delete.svg"))

        self.settings_btn=QPushButton("⚙️",self)

        self.search_btn=QPushButton("🔍",self)

        self.separator = QFrame(self)
        self.separator.setFrameShape(QFrame.Shape.HLine)
        self.separator.setFrameShadow(QFrame.Shadow.Sunken)

        self.text_edit = QTextEdit(self)
        self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: lightyellow;
                color: black;
                font-family: FiraCode Nerd Font, monospace;
                font-size: 14px;
                padding: 6px;
            }
        """)
        
        self.update_ui()

    def resizeEvent(self, event):
        self.update_ui()

    def update_ui(self):

        w = self.width()
        y = 10
        h = 30

        self.add_btn.setGeometry(10, y, 30, h)
        self.settings_btn.setGeometry(50, y, 30, h)
        self.search_btn.setGeometry(90, y, 30, h)
        self.done_btn.setGeometry(w - 80, y, 30, h)
        self.delete_btn.setGeometry(w - 40, y, 30, h)
        self.separator.setGeometry(0, y + h + 5, w, 1)
        self.text_edit.setGeometry(10,y + h + 10,w - 20, self.height() - (y + h + 20))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet("background-color: lightyellow")
    window.show()
    sys.exit(app.exec())

