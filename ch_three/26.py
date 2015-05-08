# ◑ Download some text from a language that has vowel harmony (e.g. Hungarian), extract the vowel sequences of words, and create a vowel bigram table.
import nltk
from nltk.corpus import udhr

# pulls in the universal declaration of human rights in hungarian
text = udhr.words('Hungarian_Magyar-Latin1')

def is_vowel(letter):
	"""Checks to see if a letter is a vowel."""
	if letter in "aeiou":
		return True
	else:
		return False

def pull_out_vowels(word):
	"""Takes in a word and pulls out all vowels for it."""
	vowels = []
	for letter in word:
		if is_vowel(letter):
			vowels.extend(letter)
	vowels = nltk.bigrams(vowels)
	return vowels

def vowels_for_all_words(text):
	"""pulls out all vowels for all words."""
	vowels = []

	for word in text:
		vowels.extend(pull_out_vowels(word))

	return vowels

vowel_bigrams = vowels_for_all_words(text)

cfd = nltk.ConditionalFreqDist(vowel_bigrams)
cfd.tabulate()