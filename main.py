# main.py
import sys
from PyQt6.QtWidgets import QApplication
import qt  

windows = []
style= "background-color: lightyellow;"
def addButtonClick():
    new_window = qt.MainWindow()
    new_window.setStyleSheet(style)
    windows.append(new_window)
    new_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = qt.MainWindow()
    main_window.setStyleSheet(style)
    main_window.add_btn.clicked.connect(addButtonClick)

    main_window.show()
    sys.exit(app.exec())

