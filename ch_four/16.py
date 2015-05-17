# ◑ Read up on Gematria, a method for assigning numbers to words, and for mapping between words having the same number to discover the hidden meaning of texts (http://en.wikipedia.org/wiki/Gematria, http://essenes.net/gemcal.htm).

# Write a function gematria() that sums the numerical values of the letters of a word, according to the letter values in letter_vals:

 	
# >>> letter_vals = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':80, 'g':3, 'h':8, 'i':10, 'j':10, 'k':20, 'l':30, 'm':40, 'n':50, 'o':70, 'p':80, 'q':100, 'r':200, 's':300, 't':400, 'u':6, 'v':6, 'w':800, 'x':60, 'y':10, 'z':7}
# Process a corpus (e.g. nltk.corpus.state_union) and for each document, count how many of its words have the number 666.

# Write a function decode() to process a text, randomly replacing words with their Gematria equivalents, in order to discover the "hidden meaning" of the text.

import re
from nltk.corpus import state_union
from random import random

def gematria(word):
	"""does the thing"""

	# stores all needed keys and values for conversions.

	letter_vals = {'a': '1', 'b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'80', 'g':'3', 'h':'8', 'i':'10', 'j':'10', 'k':'20', 'l':'30', 'm':'40', 'n':'50', 'o':'70', 'p':'80', 'q':'100', 'r':'200', 's':'300', 't':'400', 'u':'6', 'v':'6', 'w':'800', 'x':'60', 'y':'10', 'z':'7'}

	# splits the word into characters
	word = list(word)
	word_value = 0

	# goes through each letter and converts it to a number according to the pattern supplied above.
	for letter in word:
		for key,value in letter_vals.items():
			pattern = re.compile(key)
			letter = pattern.sub(value, letter)
		word_value += int(letter)
	return word_value

def count_devil_words(text):
	"""counts the number of words with a numerical count equal to 666. note: limited to 100000 for this particular corpus because it starts having non A-Za-z characters and will break things"""
	devil_words = 0
	for word in text[0:100000]:
		if word.isalpha(): 
			if gematria(word.lower()) == 666:
				devil_words += 1
	return devil_words

def decode(text):
	"""# Write a function decode() to process a text, randomly replacing words with their Gematria equivalents, in order to discover the "hidden meaning" of the text."""
	length = len(text)
	for i in range(0, 1000):
		num = int(random() * length)
		text[num] = gematria(str(text[num]))
	print(text)

# text = state_union.words()
text = 'counts the number of words with a numerical count equal to' * 1000
text = text.split(' ')

decode(text)
