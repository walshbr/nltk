# Write a function novel10(text) that prints any word that appeared in the last 10% of a text that had not been encountered earlier.

from nltk.corpus import nps_chat



def novel10(text):
	# finds the point at which to cut the text
	cut = int(0.9 * len(text))
	#cuts the text
	first_part, second_part = text[:cut], text[cut:]
	# makes a set of each part, leaving only unique words
	unique_words_first_part = set(first_part)
	unique_words_second_part = set(second_part)

	# makes a new list of words that only appear in the last 10%
	return [word for word in unique_words_second_part if word not in unique_words_first_part]

text = nps_chat.words()

print(novel10(text))