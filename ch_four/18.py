# ◑ Write code to print out an index for a lexicon, allowing someone to look up words according to their meanings (or pronunciations; whatever properties are contained in lexical entries).

from nltk.corpus import cmudict
from nltk.corpus import wordnet

lexicon = ['this', 'is', 'my', 'list', 'of', 'words', 'you', 'know', 'what', 'I', 'mean']

def find_pronunciations(look_up_word, pronunciations_list):
	"""Produces a list of pronunciations for a given word."""

	word_pronunciations = []

	# go through the pronunciations list. if it finds matching pronunciations, make a list of pronunciations for the word.
	for word, pron in pronunciations_list:
		if look_up_word == word:
			word_pronunciations.append(pron)
		# currently returns a tuple of pronunciations.
	return word_pronunciations 

def find_meanings(look_up_word):
	"""finds the meanings for a particular word and returns them"""
	meanings = []
	# produces definitions for every sense of the word.
	synsets = wordnet.synsets(look_up_word)
	for synset in synsets:
		meanings.append(synset.definition())
	return meanings

def produce_lexical_index(lexicon):
	"""returns a lexical index"""

	index = []
	pronunciations = cmudict.entries()

	# makes an index consisting of the pronunciations and meanings.

	for word in lexicon:
		prons = find_pronunciations(word, pronunciations)
		meanings = find_meanings(word)
		index.append((word, prons, meanings))

	return index

index = produce_lexical_index(lexicon)
for line in index:
	print(line)