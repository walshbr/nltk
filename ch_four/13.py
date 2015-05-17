# ◑ Write code to initialize a two-dimensional array of sets called word_vowels and process a list of words, adding each word to word_vowels[l][v] where l is the length of the word and v is the number of vowels it contains.

m, n = 2, 8

word_vowels = [[set() for i in range(m)] for j in range(n)]

sent = ['this', 'is', 'my', 'list', 'of', 'words']

#need to put sent somewhere in here

for lis in word_vowels:
	for word in sent:
		v = 0
		l = len(word)
		for letter in word: 
			if letter in "aeiou":
				v += 1
		word_vowels[l][v] = word

print(word_vowels)

