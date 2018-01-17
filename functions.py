import nltk
import re
import string
from collections import Counter


def opencorpus(textname):
    """Open file and return raw string

    textname    FileName.txt"""

    texopen = open(textname, 'r', encoding='utf8')
    vartext = texopen.read()
    texopen.close()
    return vartext


def tokenize_text(text):
    """Tokenize text and return sentences and words

        text    text string"""

    sentences = nltk.sent_tokenize(text)
    word_tokens = [nltk.word_tokenize(sentence) for sentence in sentences]
    return word_tokens


def filter_symb(tokens):
    """Filter symbols and return filtered tokens

            tokens   text string"""

    pattern = re.compile('[{}]'.format(re.escape(string.punctuation)))
    filtered_tokens = filter(None, [pattern.sub('', token) for token in tokens])

    return filtered_tokens