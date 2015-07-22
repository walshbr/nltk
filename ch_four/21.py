# ◑ Write a function that takes a text and a vocabulary as its arguments and returns the set of words that appear in the text but not in the vocabulary. Both arguments can be represented as lists of strings. Can you do this in a single line, using set.difference()?

from nltk.corpus import genesis

print(set(genesis.words()).difference(['this', 'is', 'my', 'vocabulary', 'lookee']))