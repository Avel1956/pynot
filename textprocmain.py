import nltk
import re
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import string
from texui import Ui_MainWindow
from functions import*
from collections import Counter
from functions import *

# C:\Users\javel\Anaconda3\Library\bin\pyuic5.bat -x mainui.ui -o texui.py

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

self.actionExit.triggered.connect(self.exitCall)


sys.exit(app.exec_())
