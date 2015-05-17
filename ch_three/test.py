# ★ With the help of a multilingual corpus such as the Universal Declaration of Human Rights Corpus (nltk.corpus.udhr), and NLTK's frequency distribution and rank correlation functionality (nltk.FreqDist, nltk.spearman_correlation), develop a system that guesses the language of a previously unseen text. For simplicity, work with a single character encoding and just a few languages.

import re

from nltk import *
from nltk.corpus import udhr
from nltk.corpus import genesis
from nltk import spearman_correlation
from nltk.corpus import gutenberg

languages = []

def prep_mystery_text(text):
	"""preps mystery text"""

	# pulls in the text whose language will be guessed.
	mystery_text = [list(word.lower()) for word in text if word.isalpha()]
	mystery_text = [item for sublist in mystery_text for item in sublist]
	fd_mystery_text = FreqDist(mystery_text)

	# pulls out a ranked list of characters based on the frequency distribution
	mystery_ranks = list(ranks_from_sequence(fd_mystery_text))

	return mystery_ranks

def prep_language_corpus(fids):
	### preps language corpus
	# pulls in all the languages, which udhr calls them the fileids)
	# fids = udhr.fileids()
	

	# makes a list of all the available languages that use Latin1 encoding.
	languages = [fileid for fileid in fids if re.findall('Latin1', fileid)]

	#pulls in all of the udhr for all diff. languages broken apart by characters.

	udhr_corpus = [[list(word.lower()) for word in udhr.words(language) if word.isalpha()] for language in languages]

	# flattens that list so that it is a clump of letters for each language

	udhr_corpus = [[item for sublist in language for item in sublist] for language in udhr_corpus]

	# gives the languages all indices. So you can pull in the text of the udhr by knowing its index number a la udhr_corpus[154] returns spanish

	languages = list(enumerate(languages))

	# gets frequency distributions for all the characters in a list. then converts it to a ranked list

	language_freq_dists = [FreqDist(language) for language in udhr_corpus]
	language_ranks = [list(ranks_from_sequence(dist)) for dist in language_freq_dists]

	return languages, language_ranks

def spearman(mystery_ranks, language_ranks):
	"""spearman correlation bit. compares the ranks for the mystery text with the ranks of every other language
"""
	spearman_numbers = [] 
	for language in language_ranks:
		number = spearman_correlation(language, mystery_ranks)
		spearman_numbers.append(number)

	return spearman_numbers


def calculate(text, fids):
	"""zips the spearman correlation numbers into a single list along with the language list and their indices."""

	languages, language_ranks = prep_language_corpus(fids)
	mystery_ranks = prep_mystery_text(text)
	spearman_numbers = spearman(mystery_ranks, language_ranks)
	zipped = list(zip(languages, spearman_numbers))

	# sorts it all by the spearman correlation, and then pops the last one (highest one) off and prints it out. That's the computer's best guess as to what is the same.

	zipped = sorted(zipped, key=lambda x: x[1])

	return zipped

if __name__ == '__main__':
	fids = ['French_Francais-Latin1', 'Spanish-Latin1', 'German_Deutsch-Latin1', 'English-Latin1']
	# fids = list(udhr.fileids())
	text = gutenberg.words('austen-emma.txt')
	answer = calculate(text, fids)
	print(answer)
