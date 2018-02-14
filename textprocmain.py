
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.uic import loadUi

import nltk
import re
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import string
from texui import Ui_MainWindow
from functions import*

CorpusRaw = []
CorpusTokenRaw = []

class guiTest(QDialog):
    def __init__(self):
        super(guiTest, self).__init__()
        loadUi('prinwin.ui', self)
        self.setWindowTitle('Ver 0.0.1: Thamsaqa')
        self.openFile.clicked.connect(self.on_pushButton_clickedfile)
        self.preProc.clicked.connect(self.on_pushButton_clickedtokenize)
        self.analysis.clicked.connect(self.on_pushButton_clickedanalysis)
        self.closeButt.clicked.connect(self.on_pushButton_clickedclose)

    @pyqtSlot()

    def on_pushButton_clickedfile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*)",
                                                  options=options)
        if fileName:
            CorpusRaw = fileName
        return CorpusRaw

    def on_pushButton_clickedtokenize(self):
        CorpusTokenRaw = tokenize_text(CorpusRaw)
        return CorpusTokenRaw

    def on_pushButton_clickedanalysis(self):
        print(len(CorpusTokenRaw))





app = QApplication(sys.argv)
widget = guiTest()
widget.show()

sys.exit(app.exec_())


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
