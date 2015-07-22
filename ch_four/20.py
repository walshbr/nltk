# ◑ Write a function that takes a list of words (containing duplicates) and returns a list of words (with no duplicates) sorted by decreasing frequency. E.g. if the input list contained 10 instances of the word table and 9 instances of the word chair, then table would appear before chair in the output list.

from nltk.book import FreqDist


words = ['this', 'is', 'my', 'list', 'of', 'list', 'of', 'list', 'is', 'this', 'of', 'list', 'of', 'list', 'of', 'list', 'of', 'list', 'of', 'words']

fdist = FreqDist(words)
length = len(set(fdist))
answer = list(fdist.most_common(length))
answer.reverse()
answer = [i[0] for i in answer]
print(answer)