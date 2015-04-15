import nltk
from nltk.corpus import udhr

files = udhr.fileids()
languages = list(x for x in files if 'Latin1' in x)

def find_language(str):
	for language in languages:
		lexicon = udhr.words(fileids=language)
		print(lexicon)

		for latin_language in lexicon:
			if str in latin_language:
				print(latin_language)

find_language("sentence")
# 	return #list of languages with that string