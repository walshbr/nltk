# ◑ Write a recursive function lookup(trie, key) that looks up a key in a trie, and returns the value it finds. Extend the function to return a word when it is uniquely determined by its prefix (e.g. vanguard is the only word that starts with vang-, so lookup(trie, 'vang') should return the same thing as lookup(trie, 'vanguard')).

words = ['yo', 'this', 'is', 'my', 'list', 'of', 'words']

def lookup(trie, key):
	return trie[key]

print(lookup(words, 'this'))