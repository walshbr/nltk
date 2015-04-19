# Read in some text from a corpus, tokenize it, and print the list of all wh-word types that occur. (wh-words in English are used in questions,
# relative clauses and exclamations: who, which, what, and so on.) Print them in order. Are any words duplicated in this list, because of the
# presence of case distinctions or punctuation

import nltk
from nltk import word_tokenize

#	reads in a text
f = open('corpus.txt')
raw = f.read()

# tokenizes that text
tokens = word_tokenize(raw)

# pulls out all the words that start with wh. and prints it out.
wh_words = [word for word in tokens if word.startswith('wh')]

# sorts the list and prints it
wh_words.sort()
print(wh_words)