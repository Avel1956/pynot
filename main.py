from PyQt5.QtWidgets import QApplication, QMainWindow

from texui import Ui_MainWindow


class Tex_Ui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Tex_Ui, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)
        self.actionExit.triggered.connect(self.close)

        # Make some local modifications.

        # Connect up the buttons.


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Tex_Ui()

    ui.show()
    sys.exit(app.exec_())
