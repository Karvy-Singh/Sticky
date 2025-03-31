import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QLabel, QFrame, QTextEdit,QPushButton,QMainWindow
)
from PyQt6.QtGui import QIcon,QGuiApplication
from PyQt6.QtCore import Qt

class Notification(QMainWindow):

    def __init__(self,value):

        super().__init__()
        coords=dim.getCoords()

        self.setWindowTitle("Notification")
        self.setWindowOpacity(0.90)
        self.setStyleSheet("background-color: lightblack")

        dismiss_btn= QPushButton("Dismiss",self)
        snooze_btn= QPushButton("Snooze",self)
        self.buttonStyle(dismiss_btn)
        self.buttonStyle(snooze_btn)
        
        text= QLabel(self)
        text.setWordWrap(True)
        text.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        text.setStyleSheet("""
                                background-color= transparent;
                                border: None;
                                color: white;
                                padding: 6px;
                                font-family: FiraCode Nerd Font, monospace;
                                font-size: 18px;
                                """)

        dismiss_btn.setGeometry(400,110,90,30)
        snooze_btn.setGeometry(300,110,90,30)
        text.setGeometry(10,10,490,100)
        text.setFixedSize(490,100)
        self.setGeometry(coords[2]-550, coords[3]-200, 500, 150)
        self.setFixedSize(500,150)

    def buttonStyle(self,btn):
        btn.setStyleSheet("""
                          color: black;
                          background-color:white;
                          """)

if __name__=="__main__":
    app=QApplication(sys.argv)
    dim=QGuiApplication.primaryScreen().availableGeometry()
    window=Notification(dim)
    window.show()
    sys.exit(app.exec())

