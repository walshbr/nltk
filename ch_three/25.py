# ◑ Pig Latin is a simple transformation of English text. Each word of the text is converted as follows: move any consonant (or consonant cluster) that appears at the start of the word to the end, then append ay, e.g. string → ingstray, idle → idleay. http://en.wikipedia.org/wiki/Pig_Latin

# Write a function to convert a word to Pig Latin. - done
# Write code that converts text, instead of individual words. - done
# Extend it further to preserve capitalization done, to keep qu together (i.e. so that quiet becomes ietquay) done, and to detect when y is used as a consonant (e.g. yellow) vs a vowel (e.g. style).

import re
import nltk
from nltk import word_tokenize

test_word = 'quiet'
test_text = 'This is my test sentence and it has so many words. Look at me!'

def word_to_pig_latin(word):
	"""takes a word and converts it to pig latin"""
	
	#matches on a cluster of consonants
	pattern = re.compile(r'^[^aeiouAEIOU]+')

	if re.findall(r'^qu', word):
		# keeps qu together a la quiet
		pattern = re.compile(r'^qu')
		beginning = re.findall(pattern, word)
		word = pattern.sub('', word)
		word += str(beginning[0]) + 'ay'
		return word

	elif re.findall(r'[^aeiouAEIOU]y[^aeiouAEIOU]', word):
		# if y has a consonant on either side it treats it like a vowel
		pattern = re.compile(r'^[^aeiouAEIOUy]+')
		beginning = re.findall(pattern, word)
		word = pattern.sub('', word)
		word += str(beginning[0]) + 'ay'
		return word

	# stores the beginning match
	elif re.findall(pattern, word):
		beginning = re.findall(pattern, word)

		#pulls out those consonants and gets rid of them
		word = pattern.sub('', word)

		#adds the consonants onto the end of the word
		word += str(beginning[0]) + 'ay'
	return word

def convert_all(text):
	"""converts all words in a given text to pig latin"""
	pig_tokens = ''

	#tokenizes the text
	tokens = word_tokenize(text)

	#regex for non-alphabetical characters
	pattern = re.compile(r'[^a-zA-Z]')

	#converts the words to pig latin and appends them to the sentence.
	for token in tokens:
		if not re.findall(pattern, token):
			word = word_to_pig_latin(token)

			if re.findall(r'[A-Z]', word):
				word = word.lower()
				word = word.capitalize()
			pig_tokens += ' ' + word
		else:
			pig_tokens += token

	pig_text = ''.join(pig_tokens)

	return pig_text



print(convert_all(test_text))
print(word_to_pig_latin('yellow'))
print(word_to_pig_latin('style'))
