#!/usr/bin/env python

"""
mdaviz: Python Qt5 application to control Bluesky Queue Server.

.. autosummary::

    ~gui
    ~main
"""

import sys

from PyQt5 import QtWidgets

from .mainwindow import MainWindow


def gui():
    """Display the main window"""

    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setStatus("Application started ...")
    main_window.show()
    sys.exit(app.exec())


def main():
    """Launch the gui."""
    gui()


if __name__ == "__main__":
    main()
