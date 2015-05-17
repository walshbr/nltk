# ◑ Write a program that takes a sentence expressed as a single string, splits it and counts up the words. Get it to print out each word and the word's frequency, one per line, in alphabetical order.

from nltk import *

def program(sent):
	"""answers the question."""
	# splits a sentence
	words = sent.split(' ')

	# gets the length of the sentence and the frequencies with which they appear.
	length = len(words)
	fd = FreqDist(words)

	# stores the frequencies and sorts them alphabetically
	frequencies = sorted(fd.most_common(length))

	#prints them out one per line.
	for frequency in frequencies:
		print(frequency)

sentence = 'this is my sentence yo what up up'

program(sentence)