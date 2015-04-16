# ☼ Save some text into a file corpus.txt. Define a function load(f) that reads from the file named in its sole argument, and returns a string containing the text of the file.

# Use nltk.regexp_tokenize() to create a tokenizer that tokenizes the various kinds of punctuation in this text. Use one multi-line regular expression, with inline comments, using the verbose flag (?x).
# Use nltk.regexp_tokenize() to create a tokenizer that tokenizes the following kinds of expression: monetary amounts; dates; names of people and organizations.

# to do: monetary amounts, dates, names of people and organizations

import nltk

def load(f):
	"""Takes a file as its argument and returns a string containing the text of that file."""
	#opens the file and loads its text in.
	t = open(f)
	t = t.read()
	return t


def tokenize_punctuation(t):
	"""Tokenizes the punctuation in a text 't'."""
	pattern = r'''(?x)			# set to be verbose
	\W 						# searches for non-alphanumeric characters.
	'''
	matches = nltk.regexp_tokenize(t, pattern)
	return matches

def tokenize_monetary(t):
	"""Tokenizes monetary amounts"""
	pattern = r'''(?x)		# sets regex to be verbose
	\d
	'''
	matches = nltk.regexp_tokenize(t, pattern)
	return matches

def tokenize_dates(t):
	"""Tokenizes dates."""

def tokenize_names(t):
	"""Tokenizes names of people and organizations."""

text = load('corpus.txt')
matches = tokenize_monetary(text)
print(matches)
print(matches[0:20])