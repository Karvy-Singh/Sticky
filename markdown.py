from PyQt6.QtWidgets import QApplication, QTextEdit, QWidget, QVBoxLayout
from PyQt6.QtGui import QTextCursor, QTextCharFormat, QFont
from PyQt6.QtCore import QObject, QEvent
import sys
import sql

def markdownify(window):
    db=sql.StickyDB()
    
    text= window.rawText.toPlainText()
    window.markdown.setMarkdown(text)

    window.markdown.show()
    window.rawText.hide()

    db.save(str(window),text)

class WindowActivityMonitor(QObject):
    def __init__(self,window):
       super().__init__()
       self.window=window

    def eventFilter(self,obj,event):
       if event.type() == QEvent.Type.WindowActivate:
           print(self.window)
       return super().eventFilter(obj,event)

