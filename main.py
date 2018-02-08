from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QFileDialog
from PyQt5 import QtGui, QtCore
from texui import Ui_MainWindow
from functions import*

data = []

class Tex_Ui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Tex_Ui, self).__init__()


        # Set up the user interface from Designer.
        self.setupUi(self)
        self.actionExit.triggered.connect(self.close)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionHistogram.triggered.connect(self.histogram)
        self.butExec.clicked.connect(self.tok)

        # Make some local modifications.

        # Connect up the buttons.

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        global data

        if fname[0]:
            f = open(fname[0], 'r', encoding='utf8')

            with f:

                data = f.read()

                self.ventPrincipal.setText(data)






    def tok(self):
        d = data
        len(d)

        if len(d) > 1:

            # from texclass import TexProp
            # consclass = TexProp('zarathustra', 1560, 50, 3)
            # wordcount = consclass.get_wordcount()
            # s = 'wordcount=' + repr(wordcount)
            # self.ventPrincipal.setText(s)

            token_list = tokenize_text(d)
            fil = [filter(None, [filter_symb(tokens)
                                 for tokens in sentence_tokens])
                   for sentence_tokens in token_list]
            fil3 = [[remove_stopwords(tokens) for tokens in sentence_tokens] for sentence_tokens in fil]
            # filteredstopwords = remove_stopwords(filteredsymbols)
            l_phrases = token_list

            l_words = []
            for list in token_list:
                for x in list:
                    l_words.append(x)
            global count_words

            count_words = Counter(l_words)
            words_frecuent = count_words.most_common(2)




            # phrase_count = Counter(l_phrases)
            # phrase_frecuent = phrase_count.most_common(1)


            word_message = 'wordcount raw = ' + repr(len(l_words))
            phrase_message = 'Phrase count raw = ' + repr(len(l_phrases))
            self.ventPrincipal.setTextColor(QtGui.QColor('red'))
            self.ventPrincipal.append('_____________________')
            self.ventPrincipal.append(word_message)
            self.ventPrincipal.append(phrase_message)
            # self.ventPrincipal.append(repr(get_nice_string(words_frecuent)))
        else:
            self.ventPrincipal.setText('Please load file')

    def histogram(self, count_words):
        from nltk import FreqDist
        fdist = FreqDist(count_words)
        fdist.plot(25, cumulative=True)






if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Tex_Ui()

    ui.show()
    sys.exit(app.exec_())
