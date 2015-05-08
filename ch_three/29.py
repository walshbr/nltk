# ◑ Readability measures are used to score the reading difficulty of a text, for the purposes of selecting texts of appropriate difficulty for language learners. 

# Let us define μw to be the average number of letters per word, and μs to be the average number of words per sentence, in a given text. 

# The Automated Readability Index (ARI) of the text is defined to be: 4.71 μw + 0.5 μs - 21.43. Compute the ARI score for various sections of the Brown Corpus, including section f (lore) and j (learned). Make use of the fact that nltk.corpus.brown.words() produces a sequence of words, while nltk.corpus.brown.sents() produces a sequence of sentences.

from nltk.corpus import brown



def average_num_words_per_sentence(text, category):
	"""returns the average number of words per sentence in a text by dividing number of words in a corpus by number of sentences in the corpus."""

	sent_num = len(text.sents(categories=category))
	word_num = len(text.words(categories=category))
	return word_num / sent_num

def average_num_letters(text, category):
	"""finds the average number of letters per word in a corpus."""

	word_num = len(text.words(categories=category))
	smash_text = ''.join(text.words(categories=category))
	letters_len = len(smash_text)

	return letters_len / word_num

def ari(text, category):
	"""Calculates the average readability of a text."""
	uw = average_num_letters(text, category)
	us = average_num_words_per_sentence(text, category)
	ari = (4.71 * uw ) + ( 0.5 * us ) - 21.43
	return ari


for category in brown.categories():
	print(category + ': ' + str(ari(brown, category)))