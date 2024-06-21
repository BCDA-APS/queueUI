from pathlib import Path

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from . import utils

class statusBar(QtWidgets.QWidgets):

    def __init__(self):
        super().__init__()
        
        self.button = QPushButton('Click me')
