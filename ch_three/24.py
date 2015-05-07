# ◑ Try to write code to convert text into hAck3r, using regular expressions and substitution, where e → 3, i → 1, o → 0, l → |, s → 5, . → 5w33t!, ate → 8. Normalize the text to lowercase before converting it. Add more substitutions of your own. Now try to map s to two different values: $ for word-initial s, and 5 for word-internal s.

import nltk
from nltk import word_tokenize
import re

#	reads in a text
f = open('corpus.txt')
raw = f.read()

# lowercases the text
raw = raw.lower()



def convert_to_hacker(text):
	"""converts a text to hacker"""
	new_text = []

	#initial pass subsitutes 8 for ate.
	pattern = re.compile(r'ate')
	text = pattern.sub('8', text) 

	# regex that searches through the text to find instances of the letters to be converted.
	pattern = re.compile(r'[eiols]|\.')


	# converts all the letters
	for w in text:
		if re.search(pattern, w):
			if w == 'e':
				w = '3'
			elif w == 'i':
				w = '1'
			elif w == 'o':
				w = '0'
			elif w == 's':
				w = '5'
			elif w == 'l':
				w = '|'
			elif w == '.':
				w = '5w33t!'
		new_text.extend(w)
	new_text = ''.join(new_text)

	# regex searching for word initial s.
	pattern = re.compile(r'\b5')
	new_text = pattern.sub('$', new_text)

	return new_text

text = convert_to_hacker(raw)
print(text)
