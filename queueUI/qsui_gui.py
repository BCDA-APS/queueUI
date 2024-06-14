"""REWRITE"""

import sys

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow


def main_gui():
    """REWRITE"""
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("My first window!")

    label = QLabel(win)
    label.setText("my first label")
    label.move(50, 50)

    win.show()
    sys.exit(app.exec_())


if __name__ == "main":
    """"""
    main_gui()
