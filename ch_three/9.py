# ☼ Save some text into a file corpus.txt. Define a function load(f) that reads from the file named in its sole argument, and returns a string containing the text of the file.

# Use nltk.regexp_tokenize() to create a tokenizer that tokenizes the various kinds of punctuation in this text. Use one multi-line regular expression, with inline comments, using the verbose flag (?x).
# Use nltk.regexp_tokenize() to create a tokenizer that tokenizes the following kinds of expression: monetary amounts; dates; names of people and organizations.

# to do: monetary amounts

import nltk
from nltk.corpus import names

# loads an list full of names
options = names.fileids()
name_options = [names.words(f) for f in options]
# flattens the list
name_options = [item for sublist in name_options for item in sublist]

def load(f):
	"""Takes a file as its argument and returns a string containing the text of that file."""
	# opens the file and loads its text in.
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
		[$£]				# searching for coin symbols.
	|	penny
	|	pennies				# searching for a variety of money words 
	|	dollars?		
	|	shillings?			
	'''
	matches = nltk.regexp_tokenize(t, pattern)
	return matches

def tokenize_dates(t):
	"""Tokenizes dates by returning months and years."""
	pattern = r'''(?x)		# sets regex to be verbose
		(January| February | March | April | May | June 
		| July | August | September 
		| October | November | December)?	# searches for a month as optional
		\s
		\d\d\d\d 			# returns four digit numbers regardless
	'''
	matches = nltk.regexp_tokenize(t, pattern)
	return matches

def tokenize_names(t):
	"""Tokenizes names of people."""
	pattern = r'''(?x)		# sets regex to be verbose
	[A-Z][a-z]+				# pulls out capitalized words				
	'''
	raw_matches = nltk.regexp_tokenize(t, pattern)
	# checks the resultant capitalized nouns against the preloaded database of names
	name_matches = [match for match in raw_matches if match in name_options]
	return name_matches

def tokenize_organizations(t):
	"""Tokenizes the names of organizations"""
	# pattern for looking for consecutive capitalized nouns on the assumption that they will
	# be organizations
	pattern = r'''(?x)		# sets regex to be verbose
	([A-Z][a-z]+\s) 			# pulls out capitalized words
	{2,}					# looks for all instances of at least two capitalized words occuring together		
	'''
	org_matches = nltk.regexp_tokenize(t, pattern)
	return org_matches

text = load('corpus.txt')
matches = tokenize_monetary(text)
print(matches)