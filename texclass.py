

class TexProp:
    """This class contains all properties of the analyzed text"""

    def __init__(self, textname, wordcount, linecount, paragraphcount):
        """Create a text instance

        textname        the name of the original file
        wordcount       number of words in the text
        linecount       number of lines in the text
        paragraphcount  number of paragraphs in the text"""

        self._textname = textname
        self._wordcount = wordcount
        self._linecount = linecount
        self._paragraphcount = paragraphcount

    def get_textname(self):
        """Return name of text"""
        return self._textname

    def get_wordcount(self):
        """Return number of words"""
        return self._wordcount

    def get_linecount(self):
        """Return number of lines in text"""
        return self._linecount

    def get_paragraphcount(self):
        """Return nnumber of paragraphs in text"""
        return self._paragraphcount


consclass = TexProp('zarathustra', 1560, 50, 3)
print(consclass.get_wordcount())
