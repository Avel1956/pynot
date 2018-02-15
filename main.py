from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtGui
from texui import Ui_MainWindow
from functions import *


data = []
fname = []
tes = []
class Tex_Ui(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Tex_Ui, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)
        self.actionExit.triggered.connect(self.close)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionHistogram.triggered.connect(self.histogram)
        self.butExec.clicked.connect(self.execute)

        # Make some local modifications.

        # Connect up the buttons.

    def openFile(self):
        global fname
        global data
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:

            f = open(fname[0], 'r', encoding='utf8')

            with f:
                data = f.read()
                self.ventPrincipal.setTextColor(QtGui.QColor('grey'))
                self.ventPrincipal.setText(data)




    def execute(self):
        d = data
        import time
        tik = time.clock()
        len(d)

        if len(d) > 1:
            

            token_list = tokenize_text(d)
            fil = [filter(None, [filter_symb(tokens)
                                 for tokens in sentence_tokens])
                   for sentence_tokens in token_list]
            fil3 = [[remove_stopwords(tokens) for tokens in sentence_tokens] for sentence_tokens in fil]
            # filteredstopwords = remove_stopwords(filteredsymbols)
            l_phrases = token_list

            l_words_raw = []
            for list in token_list:
                for x in list:
                    l_words_raw.append(x)
            global count_words_raw
            l_words_sym_fil = []
            for list in fil:
                for x in list:
                    l_words_sym_fil.append(x)
            global count_words_raw
            global count_words_symfil
            count_words_raw = Counter(l_words_raw)
            count_words_symfil = Counter(l_words_sym_fil)
            words_frecuent_raw = count_words_raw.most_common(2)
            words_frecuent_symfil = count_words_symfil.most_common(2)

            # phrase_count = Counter(l_phrases)
            # phrase_frecuent = phrase_count.most_common(1)

            tok = time.clock()
            exec_time = 'Analysis time= ' + repr(tok - tik) + ' s.'
            word_raw_message = 'wordcount raw = ' + repr(len(l_words_raw))
            phrase_raw_message = 'Phrase count raw = ' + repr(len(l_phrases))
            word_symfil_message = 'word count symbols filtered = ' + repr(len(l_words_sym_fil))
            phrase_symfil_message = 'Phrase count symbols filtered = ' + repr(len(l_phrases))
            from texclass import Book
            global tes
            try:
                tes = Book(fname[0], nochapters=False, stats=True)

            except Exception:
                self.ventPrincipal.setTextColor(QtGui.QColor('red'))
                self.ventPrincipal.append('Not recognized chapter format found')

            self.ventPrincipal.setTextColor(QtGui.QColor('green'))
            self.ventPrincipal.append('_____________________')
            self.ventPrincipal.append(exec_time)
            self.ventPrincipal.append(word_raw_message)
            self.ventPrincipal.append(phrase_raw_message)
            self.ventPrincipal.append(word_symfil_message)

            # self.ventPrincipal.append(repr(get_nice_string(words_frecuent)))
        else:
            self.ventPrincipal.setTextColor(QtGui.QColor('red'))
            self.ventPrincipal.setText('Please load file')

    def histogram(self):
        from nltk import FreqDist
        fdist = FreqDist(count_words_raw)
        fdist.plot(25, cumulative=True)



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Tex_Ui()

    ui.show()
    sys.exit(app.exec_())
