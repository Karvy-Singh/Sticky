import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QTabWidget, QPushButton,
    QTextEdit, QFrame, QVBoxLayout, QHBoxLayout
)
from PyQt6.QtGui import QIcon, QShortcut, QKeySequence
from PyQt6.QtCore import QObject, QEvent

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(10, 10, 400, 400)
        self.setMinimumSize(400, 400)
        self.setWindowTitle("Sticky Notes")

        self.tabs = QTabWidget(self)
        self.notesTab = QWidget()
        self.reminderTab = QWidget()
        self.tabs.addTab(self.notesTab, "Notes")
        self.tabs.addTab(self.reminderTab, "Remind")

        self.add_btn = QPushButton("✚", self)
        self.done_btn = QPushButton(self)
        self.done_btn.setIcon(QIcon("./assets/checkmark.svg"))
        self.delete_btn = QPushButton(self)
        self.delete_btn.setIcon(QIcon("./assets/delete.svg"))
        self.settings_btn = QPushButton("⚙️", self)
        self.search_btn = QPushButton("🔍", self)

        self.rawText= self.WritingSpace()
        self.markdown= self.WritingSpace()
        self.remind= self.WritingSpace()

        self.markdown.setReadOnly(True) 

        self.layout1 = QVBoxLayout()
        self.layout1.addWidget(self.rawText)
        self.layout1.addWidget(self.markdown)
        self.notesTab.setLayout(self.layout1)

        self.layout2 = QVBoxLayout()
        self.layout2.addWidget(self.remind)
        self.reminderTab.setLayout(self.layout2)

        self.markdown.show()
        self.rawText.hide()

        def hideNshow():
            self.markdown.setVisible(not self.markdown.isVisible())
            self.rawText.setVisible(not self.rawText.isVisible())

        self.shortcut_insert = QShortcut(QKeySequence('i'), self)
        self.shortcut_insert.activated.connect(lambda:hideNshow())

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
        text_edit = QTextEdit(self)
        text_edit.setStyleSheet("""
            QTextEdit {
                background-color: pink;
                color: black;
                font-family: FiraCode Nerd Font, monospace;
                font-size: 14px;
                padding: 6px;
                border: None;
            }
        """)
        return text_edit


