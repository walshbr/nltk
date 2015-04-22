# ◑ Are you able to write a regular expression to tokenize text in such a way that the word don't is tokenized into do and n't? Explain why this regular expression won't work: «n't|\w+».

import nltk
from nltk import word_tokenize
import re

#	reads in a text
f = open('corpus.txt')
raw = f.read()


matches = re.findall(r'\b(do)(n\'t)', raw)
print(matches)

# the regex it gives won't work because it doesn't escape the single quote. also because it's looking for either n't or one or more word characters. SO it'll return everyhing