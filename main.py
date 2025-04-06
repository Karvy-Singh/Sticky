# main.py
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtCore
from PyQt6.QtCore import QObject, QEvent
import qt 
import markdown

windows = []
monitors = []

style= "background-color: lightyellow;"

def addButtonClick():
    new_window = qt.MainWindow()
    new_window.activateWindow()
   
    new_window.setStyleSheet("background-color: pink;")
    windows.append(new_window)
    new_window.add_btn.clicked.connect(addButtonClick)
    new_window.done_btn.clicked.connect(lambda:doneButtonClick(new_window))

    monitor = markdown.WindowActivityMonitor(new_window)
    new_window.installEventFilter(monitor)
    monitors.append(monitor)

def doneButtonClick(window):
    markdown.markdownify(window)

if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = qt.MainWindow()
    monitor = markdown.WindowActivityMonitor(main_window)
    main_window.installEventFilter(monitor)

    monitors.append(monitor)

    main_window.setStyleSheet(style)
    main_window.add_btn.clicked.connect(addButtonClick)
    main_window.done_btn.clicked.connect(lambda:doneButtonClick(main_window))
    windows.append(main_window)
    main_window.show()
    sys.exit(app.exec())

