from PyQt6.QtWidgets import QApplication, QTextEdit, QWidget, QVBoxLayout
from PyQt6.QtGui import QTextCursor, QTextCharFormat, QFont
from PyQt6.QtCore import QObject, QEvent
import sys
import sql

def markdownify(window):
    db=sql.StickyDB()
    
    text= window.rawText.toPlainText()
    print(text)
    db.save(str(window),text)

    window.markdown.setMarkdown(db.read(str(window)))

    window.markdown.show()
    window.rawText.hide()

class WindowActivityMonitor(QObject):
    def __init__(self,window):
       super().__init__()
       self.window=window

    def eventFilter(self,obj,event):
       if event.type() == QEvent.Type.WindowActivate:
           print(self.window)
       return super().eventFilter(obj,event)

