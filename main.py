from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QFileDialog
from PyQt5 import QtGui, QtCore
from texui import Ui_MainWindow
from functions import*


class Tex_Ui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Tex_Ui, self).__init__()

        data = []
        # Set up the user interface from Designer.
        self.setupUi(self)
        self.actionExit.triggered.connect(self.close)
        self.actionOpen.triggered.connect(self.openFile)
        self.butExec.clicked.connect(self.tok)

        # Make some local modifications.

        # Connect up the buttons.

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            f = open(fname[0], 'r', encoding='utf8')

            with f:
                data = f.read()
                self.ventPrincipal.setText(data)


    def tok(self):
        d = self.ventPrincipal.toPlainText()
        
        if len(d) > 1:

            from texclass import TexProp
            consclass = TexProp('zarathustra', 1560, 50, 3)
            wordcount = consclass.get_wordcount()
            s = 'wordcount=' + repr(wordcount)
            self.ventPrincipal.setText(s)
        self.ventPrincipal.setText('load file')
        return s







if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Tex_Ui()

    ui.show()
    sys.exit(app.exec_())
