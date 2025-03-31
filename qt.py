import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QTabWidget, QPushButton,
    QTextEdit, QFrame, QVBoxLayout, QHBoxLayout
)
from PyQt6.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(10, 10, 400, 400)
        self.setMinimumSize(400, 400)
        self.setWindowTitle("Sticky Notes")

        self.tabs = QTabWidget(self)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab1, "Notes")
        self.tabs.addTab(self.tab2, "Remind")

        self.add_btn = QPushButton("✚", self)
        self.done_btn = QPushButton(self)
        self.done_btn.setIcon(QIcon("checkmark.svg"))
        self.delete_btn = QPushButton(self)
        self.delete_btn.setIcon(QIcon("delete.svg"))
        self.settings_btn = QPushButton("⚙️", self)
        self.search_btn = QPushButton("🔍", self)

        space1= self.WritingSpace()
        space2= self.WritingSpace()

        layout1 = QVBoxLayout()
        layout1.addWidget(space1)
        self.tab1.setLayout(layout1)

        layout2 = QVBoxLayout()
        layout2.addWidget(space2)
        self.tab2.setLayout(layout2)

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
        self.tabs.setGeometry(0, y + h + 10, w, self.height() - (y + h + 10))

    def WritingSpace(self):
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
        return self.text_edit

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet("background-color: lightyellow")
    window.show()
    sys.exit(app.exec())

