# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import matplotlib
import numpy
import nltk
import re
import string
import csv
from nltk.corpus import gutenberg
from collections import Counter
from pprint import pprint

"""
Importacion de corpus
"""
"""
mob=gutenberg.raw(fileids='melville-moby_dick.txt')
"""
mar = open('literature_moby.txt', 'r', encoding='utf8')
mart = mar.read()
mar.close()
texrec = open('filosofia_zara.txt', 'r', encoding='utf8')
texrect = texrec.read()
texrec.close()
corpus = [mart, texrect]
"""
Tokenizacion
frases definicion
"""


def tokenize_text(text):
    sentences = nltk.sent_tokenize(text)
    word_tokens = [nltk.word_tokenize(sentence) for sentence in sentences]
    return word_tokens


"""
separacion por frases y palabras
"""
token_list = [tokenize_text(text) for text in corpus]

"""
Filtrar simbolos especiales def
"""


def filter_symb(tokens):
    pattern = re.compile('[{}]'.format(re.escape(string.punctuation)))
    filtered_tokens = filter(None, [pattern.sub('', token) for token in tokens])
    return filtered_tokens


"""
Filtrar simbolos especiales 
"""
fil = [filter(None, [filter_symb(tokens)
                     for tokens in sentence_tokens])
       for sentence_tokens in token_list]

"""
Filtrar palabras no relevantes def
"""


def remove_stopwords(tokens):
    stopword_list = nltk.corpus.stopwords.words('english')
    filtered_tokens = [token for token in tokens if token not in stopword_list]
    return filtered_tokens


"""
Filtrar palabras no relevantes 
"""

fil3 = [[remove_stopwords(tokens) for tokens in sentence_tokens] for sentence_tokens in fil]

"""
Reconstruccion vector de palabras por texto en el corpus
"""
m = []
for list in fil3[0]:
    for x in list:
        m.append(x)

t = []
for list in fil3[1]:
    for x in list:
        t.append(x)
"""
Conteo de ocurrencia de palabras
"""

ocm = Counter(m)
comm = ocm.most_common(30)

octt = Counter(t)
comt = octt.most_common(30)
"""
Guardar conteo de ocurrencias en .csv
"""
with open('moby.csv', encoding='utf-8-sig', mode='w') as fp:
    fp.write('pal|freq\n')
    for tag, count in ocm.items():
        fp.write('{}|{}\n'.format(tag, count))

with open('zara.csv', encoding='utf-8-sig', mode='w') as fp:
    fp.write('pal|freq\n')
    for tag, count in octt.items():
        fp.write('{}|{}\n'.format(tag, count))

"""
Frecuencia
"""
from nltk import FreqDist

fdist1 = FreqDist(ocm)
fdist1.plot(25, cumulative=True)

fdist2 = FreqDist(octt)
fdist2.plot(25, cumulative=True)
"""
Mapa de dispersión
"""
from nltk.text import Text

textListNLTK = Text(m)
textListNLTK.concordance('also')
marcommon = []
for list in comt[0:30]:
    for word in list[0]:
        marcommon.append(word)
"""
textListNLTK.dispersion_plot([comm[5:8][0]])

"""
