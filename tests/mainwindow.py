import pathlib
import sys
import PyQt5

from PyQt5 import *
from pathlib import Path

UiFile = #path to the mainwinwod.ui file qsui/resources/mainwindow.ui

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()
        
        # uic.loadUi("mainwindow.ui", self)
