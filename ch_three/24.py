# ◑ Try to write code to convert text into hAck3r, using regular expressions and substitution, where e → 3, i → 1, o → 0, l → |, s → 5, . → 5w33t!, ate → 8. Normalize the text to lowercase before converting it. Add more substitutions of your own. Now try to map s to two different values: $ for word-initial s, and 5 for word-internal s.

import nltk
from nltk import word_tokenize
import re

#	reads in a text
f = open('corpus.txt')
raw = f.read()

# lowercases the text
raw = raw.lower()

# regex that searches through the text to find instances of the letters to be converted.
pattern = re.compile(r'[eiols]|ate')


# print(pattern.sub('', raw))