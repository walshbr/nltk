# ◑ Write a function shorten(text, n) to process a text, omitting the n most frequently occurring words of the text. How readable is it?

from nltk.corpus import gutenberg
from nltk import FreqDist

text = [word for word in gutenberg.words('austen-emma.txt')]

def shorten(text, n):
	"""Does the thing"""
	words_to_omit = omitted_words(text, n)

	new_text = []

	# makes a new text consisting of the text minus the old words.

	for word in text:
		if word not in words_to_omit:
			new_text.append(word)
		else:
			new_text.append('___')
			
	new_text = ' '.join(new_text)
	
	return new_text

def omitted_words(text, n):
	"""returns the n most common words in a text that will be omitted"""
	fd = FreqDist(text)
	words = [word for (word,_) in fd.most_common(n)]
	return words

text = shorten(text, 10)
print(text)