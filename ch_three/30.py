# ◑ Use the Porter Stemmer to normalize some tokenized text, calling the stemmer on each word. Do the same thing with the Lancaster Stemmer and see if you observe any differences.

import nltk
from nltk.corpus import genesis

text = genesis.words()
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()


for word in text:
	print(word)
	print("porter: " + porter.stem(word))
	print("lancaster: " + lancaster.stem(word))