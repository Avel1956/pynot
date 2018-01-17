
import nltk
import re
import string
from collections import Counter
from functions import*

CorpusRaw = opencorpus(input())
CorpusTokenRaw = tokenize_text(CorpusRaw)
print(len(CorpusTokenRaw))

