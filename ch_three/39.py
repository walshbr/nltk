# √ Retain the first letter of the name and drop all other occurrences of a, e, i, o, u, y, h, w.
#consonant conversion.
# If two or more letters with the same number are adjacent in the original name (before step 1), only retain the first letter; also two letters with the same number separated by 'h' or 'w' are coded as a single number, whereas such letters separated by a vowel are coded twice. This rule also applies to the first letter.
# Iterate the previous step until you have one letter and three numbers. If you have too few letters in your word that you can't assign three numbers, append with zeros until there are three numbers. If you have more than 3 letters, just retain the first 3 numbers.

import re

word = 'sentence'

def pattern_conversion(conversion_pairing, word):
	"""takes in a tuple consisting of a regex pattern and the thing to convert the matches to. And its second parameter is the word that is beind processed. returns a converted word."""
	pattern = re.compile(r'(' + conversion_pairing[0] + ')')
	processed_word = pattern.sub(conversion_pairing[1], word)
	return processed_word

def convert_consonants(rest_of_word):
	"""converts all consonants according to the above parameters. step two in the instructions."""
	consonant_conversions = [['[bfpv]', '1'], ['[cgjkqsxz]', '2'], ['[dt]', '3'], ['l', '4'], ['[mn]', '5'], ['r', '6']]

	for conversion in consonant_conversions:
		rest_of_word = pattern_conversion(conversion, rest_of_word)
	return rest_of_word

def drop_letters(rest_of_word):
	"""drops all non-first letter occurrences of the predetermined letters. step one in the instructions."""
	drop_letters = ['[aeiouyhw]', '']
	rest_of_word = pattern_conversion(drop_letters, rest_of_word)

	return rest_of_word

def adjacent_check(word):
	"""If two or more letters with the same number are adjacent in the original name (before step 1), only retain the first letter; also two letters with the same number separated by 'h' or 'w' are coded as a single number, whereas such letters separated by a vowel are coded twice. This rule also applies to the first letter."""

	#If two or more letters with the same number are adjacent in the original name (before step 1), only retain the first letter

	adjacent_conversion = [r'(.)\1', '']
	# problem i'm getting here = it's giving \0x1 because it's not being passed a raw string. thoughts?
	
	# tried making it take the raw string, but it's responding with "sre_constants.error: cannot refer to open group"


	print(word)

	#also two letters with the same number separated by 'h' or 'w' are coded as a single number, whereas such letters separated by a vowel are coded twice. 

def soundex(word):


	first_letter = word[0]
	rest_of_word = word[1:]
	rest_of_word = convert_consonants(rest_of_word)

word = adjacent_check('parrot')
print(word)